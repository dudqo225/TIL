# Algorithm | 백준 2609.최대공약수와 최소공배수 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 2609.최대공약수와 최소공배수 링크](https://www.acmicpc.net/problem/2609)

</br>

#### 문제

두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

</br>

#### 코드

```python
# 최대공약수
def GCD_MOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

# 최소공배수
def LCM(a, b, gcd):
    return a * b // gcd

A, B = map(int, input().split())

gcd = GCD_MOD(A, B)
lcm = LCM(A, B, gcd)

print(gcd)
print(lcm)
```

</br>

#### 풀이

```python
최대공약수란? GCD(Greatest Common Divisor)
두 자연수의 공통된 약수 중 가장 큰 수를 의미한다.

최소공배수란? LCM(Least Common Multiple)
두 자연수의 공통된 배수 중 가장 작은 수를 의미한다.
최소공배수 = 두 자연수의 곱 / 최대공약수

즉, 두 자연수가 주어지고 최대공약수를 구할 수 있으면 최소공배수도 쉽게 구할 수 있다.

최대공약수를 아래 '참고'의 블로그 내용을 확인하여 구현하였다.
<방법>
1. 유클리드 알고리즘 - 큰 수에서 작은 수를 빼서 한 개의 수가 0이 될 때까지 계산
2. 유클리드 알고리즘의 뺄셈 연산을 나머지 연산(%)으로 바꾸어 반복 횟수를 줄임
3. 재귀함수를 이용하여 계산

2번째 방법을 사용하여 최대공약수를 구하였다.
```



##### 참고

https://myjamong.tistory.com/138

https://chanos.tistory.com/entry/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%B5%9C%EC%B4%88%EC%9D%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%B5%9C%EB%8C%80-%EA%B3%B5%EC%95%BD%EC%88%98-%EA%B3%84%EC%82%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95



✨ 최대공약수, 최소공배수 개념은 초등학교?중학교 때 배웠던 내용인 것 같다. 개념을 다시한 번 정립할 수 있었고, 파이썬 언어의 while 문을 사용하여 코드 구현하는 것을 연습할 수 있는 기회였다고 생각한다. 2021.12.25

