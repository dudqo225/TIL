# Algorithm | 백준 2108.통계학 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 2108.통계학 링크](https://www.acmicpc.net/problem/2108)

</br>

#### 문제

수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

</br>

#### 코드

```python
from collections import Counter

N = int(input())

numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)

numbers.sort()
# 산술평균
ans_1 = round(sum(numbers) / N)

# 중앙값
ans_2 = numbers[N//2]

# 최빈값
cnt = Counter(numbers).most_common(2)

if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        ans_3 = cnt[1][0]
    else:
        ans_3 = cnt[0][0]
else:
    ans_3 = cnt[0][0]

# 범위
ans_4 = max(numbers) - min(numbers)

print(ans_1)
print(ans_2)
print(ans_3)
print(ans_4)
```

</br>

#### 풀이

```python
산술평균, 중앙값, 범위는 쉽게 해답을 구할 수 있다.

3번째 최빈값이 다소 난해했는데, 최빈값이 여러개일 경우 두번째로 작은 수를 뽑아내는 것이 관건이다.
파이썬 내장 collections의 Counter 함수와 .most_common() 메서드를 사용해서 최빈값을 뽑아낸다.
.most_common()의 결과를 보면 튜플 형태로 값이 들어온다.
튜플의 0번째 값은 해당 value이고, 1번째 값은 빈도수이다.
if~else 분기처리를 통해서 최빈값을 뽑아낸다.
```



✨기본적으로 입력받는 input() 값을 활용하여 평균, 중앙값, 최빈값, 범위(최대-최소) 를 구하는 문제이다.

위 풀이에도 썼듯이, 최빈값을 구하는 부부닝 난해했다. 고민고민해도 해결되지 않아 검색을 통해 `colllections`의 `Counter` 함수를 사용하여 문제를 해결하면 되는 것을 알게 되었다.



##### 참고

https://somjang.tistory.com/entry/BaekJoon-2108%EB%B2%88-%ED%86%B5%EA%B3%84%ED%95%99-Python

