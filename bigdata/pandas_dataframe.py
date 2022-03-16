import pandas as pd

# 첫 번째 Data Frame 생성
df1 = pd.read_excel("./profile_exercise.xlsx")

# .head() 메서드로 데이터 일부 확인
df1.head(5)

# 두 번째 Data Frame 생성
df2 = pd.read_excel("./exercise.xlsx")

# .drop() 메서드를 이용. 필요 없는 Column 삭제
df1 = df1.drop(["SPORTS_STEP_NM","FLAG_ACCTO_RECOMEND_MVM_RANK_CO"], axis=1)

# gender 열의 데이터 중 "M" 인 데이터를 "남"으로, "F" 인 데이터를 "여"로 변경
df1.loc[df1["gender"] == "M", "gender"] = "남"
df1.loc[df1["gender"] == "F", "gender"] = "여"

# level 열의 데이터를 변경
df1.loc[df1["level"] == "참가증", "level"] = 4
df1.loc[df1["level"] == "1등급", "level"] = 1
df1.loc[df1["level"] == "2등급", "level"] = 2
df1.loc[df1["level"] == "3등급", "level"] = 3

# df1의 데이터 중 모든 Column에 대해 데이터가 중복되는 행 삭제
df1 = df1.drop_duplicates()

# 데이터 프레임 간 병합(DB의 조인 개념)
df3 = pd.merge(left = df1 , right = df2, how = "left", on = "name")

# 필요없는 name Column 삭제
df3 = df3.drop(["name"], axis=1)

# 이름이 id인 Column을 exercise_id로 변경
df3.rename(columns = {"id": "exercise_id"}, inplace = True)

# Data Frame을 Excel 파일로 저장
df3.to_excel("./result_exercise.xlsx")