### python | dictionary Indexing



2021.07.23

연습문제를 푸는데 자꾸 아래와 같은 `TypeError`가 나온다.

```python
TypeError: list indices must be integers or slices, not list
```

뭐가 문제지? 살펴보니, `list` 안에 `dictionary` 가 포함되어 있는 다소 복잡한 구조에서 `indexing` 할 때 빈번히 발생하는 문제였다. (나만 모르는게 아니었군😐)

남들이 알아보기 쉽게 정리하기는 어렵고, 내가 나중에 봐도 알기 쉽게 간단한 예시를 작성하겠다.

### List 안에 있는 Dictionary key, Value에 접근하기

```python
# List 안에 Dictionary 가 있는 경우
movies = [
    {
        'title': '인셉션',
        'genre': '미스터리',
        'release_date': '2016-07-01',
    },
    {
        'title': '타이타닉',
        'genre': '일반',
        'release_date': '2001-02-05',
    },
    {
        'title': '해리포터',
        'genre': '판타지',
        'release_date': '2005-04-07',
    }
]
```

```python
type(movies) >>> list
type(movies[0]) >>> dict
```

`movies` 의 `type` 을 확인하면 리스트가 나오고, 인덱싱을 통해 `movies[0]`의 `type`을 확인하면 딕셔너리가 나온다.



```python
# 반복문을 돌릴 경우
for movie in movies:
    print(movie['title'])

[결과]
인셉션, 타이타닉, 해리포터
```

반복문 내의 `movie` 는 하나의 `dictionary` 가 된다.



```python
# 중첩 반복문
for movie in movies:
    for key, value in movie.items():
        print(key, value)
        
[결과]
title 인셉션
genre 미스터리
release_date 2016-07-01
title 타이타닉
genre 일반
release_date 2001-02-05
title 해리포터
genre 판타지
release_date 2005-04-07
```

`movie` 딕셔너리에 `.items()` 메소드를 사용하여 각각의 `key`, `value` 값을 가져올 수 있다.



> 몇 번 반복해서 문제를 풀어보니 사실 쉬운 부분이었다. 디버깅을 중간중간 하면서 접근하면 간단하다. 😄