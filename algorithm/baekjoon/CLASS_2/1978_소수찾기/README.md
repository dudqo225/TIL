# Algorithm | 백준 1978.소수 찾기 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 1978.소수 찾기 링크](https://www.acmicpc.net/problem/1978)

</br>

#### 문제

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

</br>

#### 코드

```python
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

N = int(input())
n_list = list(map(int, input().split()))

ans = 0
for n in n_list:
    if n > 1:
        check = is_prime_number(n)
        if check == True:
            ans += 1

print(ans)
```

</br>

#### 풀이

```python
소수란?
1과 자기 자신 외의 약수를 가지지 않고, 1보다 큰 자연수

입력받은 N개의 자연수 리스트를 순회하면서, 소수인지 여부를 판단한다.

1. is_prime_number(x) 함수는 for문으로 동작한다. 
2. i를 2부터 x-1까지 1씩 증가시키면서 자연수 x가 i로 나누어 떨어지면, i는 x의 약수이기 때문에 소수가 아니다. 따라서 False를 리턴하면서 함수를 종료한다.
3. 만일 for문 반복을 완료한다면 소수이기 때문에 True를 리턴한다.
4. is_prime_number(x) 함수의 리턴값을 check 변수에 저장하고, 해당 변수가 True라면 소수이기 때문에 ans를 1 증가시킨다.
```



✨ 이 문제처럼 기초 수학을 알고리즘화하여 코드로 구현하는 것이 매우 중요하다. 기초적인 구현이 가능해야 더 어려운 알고리즘 문제도 풀 수 있다! 2021.12.24

