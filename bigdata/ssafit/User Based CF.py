# 코드 실행시간 체크
import time
# DB 연결
import mariadb
from sqlalchemy import create_engine
import pymysql
# 데이터 분석 및 추천 알고리즘 구현
import pandas as pd
import math
from sklearn.metrics.pairwise import cosine_similarity

# 코드 시작 시간
start = time.time()

'''
Python - MariaDB 연결
'''
# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()

# MariaDB 연결
conn = mariadb.connect(
    user='username',
    password='password',
    database='db_name',
    host='hostname/ip',
    port=3306
)

# DB 엔진 생성
engine = create_engine("mysql://{username}:{password}@{host IP}/{db_name}".format(user='username', pw='password', db='db_name'))

# 커서 생성
cs = conn.cursor()

# 추천 테이블 기존 데이터 삭제
del_sql = "TRUNCATE similarity_recommendation"
cs.execute(del_sql)

# 운동 이력 테이블 불러오기
select_sql = "SELECT user_id, exercise_id, COUNT(*) FROM exercise_history GROUP BY exercise_id"
cs.execute(select_sql)
history_table = cs.fetchall()
# 운동 이력 테이블 → 데이터프레임 변경
history_df = pd.DataFrame(history_table, columns=['user_id', 'exercise_id', 'cnt'])


# 즐겨찾기 테이블 불러오기
select_sql2 = "SELECT user_id, exercise_id, 1 FROM exercise_bookmark"
cs.execute(select_sql2)
bookmark_table = cs.fetchall()
# 즐겨찾기 테이블 → 데이터프레임 변경
bookmark_df = pd.DataFrame(bookmark_table, columns=['user_id', 'exercise_id', 'rating'])


'''
Cold Start Problem 해결을 위한 Dummy Data 활용
'''
# 운동 이력 Dummy Data
dummy_count = pd.read_csv('./dummy_count.csv')

# 운동 즐겨찾기 Dummy Data
dummy_bookmark = pd.read_csv('./dummy_bookmark.csv')

# 운동 데이터
exercise = pd.read_excel('./exercise.xlsx')

# Dummy Data + DB 운동 이력 데이터
dummy_count = pd.concat((dummy_count, history_df), ignore_index=True)

# Dummy Data + DB 운동 즐겨찾기 데이터
dummy_bookmark = pd.concat((dummy_bookmark, bookmark_df), ignore_index=True)


'''
운동 이력 (Exercise History)
'''
# 사용자 ID별 운동 횟수 총합
grouped = dummy_count.groupby(dummy_count["user_id"]).sum().drop("exercise_id", axis=1)

# 사용자 운동횟수 비율 구하기
df = pd.merge(dummy_count, grouped, left_on=['user_id'], right_on=['user_id'], how='left')
df['proportion'] = round(df['cnt_x']/df['cnt_y']*100, 2)

# Column 명 변경
df.rename(columns = {'cnt_x':'cnt', 'cnt_y':'total_cnt'}, inplace=True)


# 평점 구하는 함수
def get_rating(x):
    if (x > 18):
        rating = 5
    elif (13.5 < x <= 18):
        rating = 4
    elif (9 < x <= 13.5):
        rating = 3
    elif (4.5 < x <= 9):
        rating = 2
    else:
        rating = 1
    return rating*0.8


# 데이터프레임에 평점(rating) 추가. apply() 적용
df['rating'] = df['proportion'].apply(lambda x : get_rating(x) )


'''
운동 즐겨찾기 (Exercise Bookmark)
'''
# 즐겨찾기 + 운동 이력 Merge
df2 = pd.merge(df, dummy_bookmark, left_on=['user_id', 'exercise_id'], right_on=['user_id', 'exercise_id'], how='left')

# 빈 데이터 0으로 채우기
df2.fillna(0, inplace=True)

# 운동 이력 평점 + 즐겨찾기 평점 → rating Column
df2['rating'] = df2['rating_x'] + df2['rating_y']

# 필요없는 Column 삭제
df2.drop(['rating_x', 'rating_y'], axis=1)

# Pivot Table 변경
df2 = df2.pivot_table('rating', index='user_id', columns='exercise_id')

# 중간 생략없이 모든 데이터 보여주기 (Pandas Option)
# pd.set_option('display.max_columns', None)

# df2의 비어있는 데이터를 0으로 채우고 df3에 할당
df3 = df2.fillna(0)

# df3 데이터프레임을 활용하여 사용자 간 코사인 유사도 계산
cos_sim = cosine_similarity(df3)

# 코사인 유사도 계산 결과를 DataFrame으로 변경
cos_sim_mat = pd.DataFrame(data=cos_sim, index=df3.index, columns=df3.index)


'''
유사도 기반 운동 추천 알고리즘
'''
def recommendExercise(user_id, dataframe, sim_mat):
    # exercises 안에 user_id 사용자가 수행한 운동ID만 담는다.
    exercises = []
    for i in dataframe.loc[user_id,:].index:
        if math.isnan(dataframe.loc[user_id,i]) == False:
            exercises.append(i)
    
    # U_df는 user_id 사용자가 한 운동만 추출
    U_df = pd.DataFrame(dataframe.loc[user_id, exercises]).T
    
    # sim_dict에 user_id와 다른 사용자 간의 유사도를 평가한 결과를 담는다.
    sim_dict = sim_mat[user_id].to_dict()
    
    # 추천 운동 출력 #
    import operator
    
    sim_mat = sorted(sim_dict.items(), key=operator.itemgetter(1), reverse=True)
        
    # user_id 사용자가 하지 않은 운동 추출
    recommend_list = list(set(dataframe.columns) - set(U_df.columns))
    
    others_k = [i[0] for i in sim_mat]
    
    recommender = {}
    
    for exercise in recommend_list:
        rating = []
        sim = []
        
        for person in others_k:
            if math.isnan(dataframe.loc[person, exercise]) == False:
                rating.append(dataframe.loc[person, exercise])
                sim.append(sim_dict[person])
        
        # KNN - K : 3
        pred = ((sim[0]*rating[0]) + (sim[1]*rating[1]) + (sim[2]*rating[2])) / (sum(sim[:3]))
        
        recommender[exercise] = round((pred + 5) * 10)
    
    rec_dic = {"rec_list": "{}".format(dict(sorted(recommender.items(), key=operator.itemgetter(1), reverse=True)[:10]))}

    return rec_dic

# 추천 결과 저장을 위한 DataFrame 초기화
data = pd.DataFrame()

# Dummy Data 60개를 제외한 사용자 ID 리스트 순회
for i in list(cos_sim_mat.index)[:-60]:
    rec_list = pd.DataFrame(recommendExercise(i, df2, cos_sim_mat), index=[i])
    data = pd.concat((data, rec_list), sort=False)

# 추천 결과를 itertuples로 하여 리스트 형태로 data1에 저장
data1 = list(data.itertuples(index=True, name=None))

# similarity_recommendation 테이블에 데이터 추가를 위한 SQL문 작성
sql = """
INSERT INTO ssafit_test.similarity_recommendation (
    user_id,
    exercise_id
) VALUES (
    ?, ?
)
"""

# SQL 실행 후 저장
# .executemany() → 복수개의 Tuple 데이터 실행
cs.executemany(sql, data1)
# .commit()을 하지 않으면 데이터 변경 X
conn.commit()

# DB 연결 종료
conn.close()

# 코드 종료 시간
end = time.time()

# 코드 수행 시간 출력
print("time: {}".format(end-start))
