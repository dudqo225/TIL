# Bigdata | Day1_PJT Intro



넷플릭스, 유튜브 등 많은 글로벌 기업이 추천 시스템을 통해서 이익을 창출

<br>

영화 평점 빅데이터를 이용하여 **협업 필터링(Collaborative Filtering) 알고리즘**을 구현, Python 언어를 활용

<br>

#### Collaborative Filtering

- K-nearest neighbor (KNN) 알고리즘
- Matrix factorization 알고리즘
- Matrix factorizatoin + PLSI 알고리즘

<br>

**Probabilistic Modeling** 기술을 습득

Django를 이용하여 UI 구현

<br>

***

<br>

### PJT 템플릿 설치

<br>

##### Anaconda 

- 파이썬 관련 오픈소스, 편리한 사용이 가능함

<br>

**Gitlab** 에서 프로젝트 클론 후 실행해보기

```python
python manage.py migrate
python manage.py runserver
```

<br>

***

<br>

### Django 알아보기

<br>

클라이언트에서 요청(Request)이 넘어오면,

- `urls` 에서 특정 요청을
- `views` 로 보내고, 데이터가 필요할 경우
- `models` 에서 가져와
- `templates` 에 전달하고,

클라이언트에 응답(Response) 한다.

<br>

기본적인 MVC 패턴을 가지기 때문에, 자바 - 스프링과 크게 다를 것이 없다.

<br>

***

<br>

### 1일차 과제

<br>

```py
def load_recomm(cur, model_home):
    path = join(model_home, 'recommend_ratings.txt')
    cur.execute('DELETE FROM movieRec_recomm')
    with open(path) as f:
        for line in f:
            token = line.strip().split('::')
            cur.execute('INSERT INTO movieRec_recomm(user_id, movie_id, score) VALUES(?,?,?)', token)
```

- 추천 알고리즘에서 생성한 추천 결과를 읽어옴
- SQLite3 DB에 있는 `movieRec_recomm` 테이블 내용을 삭제
- 예상 평점이 있는 `recommend_ratings.txt` 파일은 `user_id::movie_id::score` 형태로 저장되어 있음
  - 이 데이터를 읽어서 각각 `user_id`, `movie_id`, `score`를 SQLite3 DB의 `movieRec_recomm` 테이블에 삽입한다.