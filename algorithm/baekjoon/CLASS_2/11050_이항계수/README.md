# Algorithm | 백준 11050.이항계수 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 11050.이항계수 링크](https://www.acmicpc.net/problem/11050)

</br>

#### 문제

자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램을 작성하시오. 
$$
\binom{N}{K}
$$
</br>

#### 코드

```python
def bino_coef(n, k):
    if k == 0 or n == k:
        return 1
    return bino_coef(n-1, k) + bino_coef(n-1, k-1)

N, K = map(int, input().split())

ans = bino_coef(N, K)

print(ans)
```

</br>

#### 풀이

```python
이항계수란,
주어진 크기 집합에서 원하는 개수를 순서없이 뽑는 즉, 조합을 의미한다.
'이항'이란 뽑거나 / 안뽑거나 두 가지 선택지가 있음을 의미한다.
```



#### 참고

[참고 깃허브 블로그](https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients)

위 블로그에 이항계수의 개념과 이항계수를 구현하는 3가지 코드에 대해서 잘 정리되어 있다.



✨ 수학관련 알고리즘 문제는 항상 어렵다. 그때마다 인터넷에 개념이나 관련 알고리즘 구현 코드가 상세히 나와있기 때문에 공부할 수 있어서 유용하다.
