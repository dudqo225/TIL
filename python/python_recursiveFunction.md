# python | Recursive function (재귀함수)

> **함수 내부에서 자기 자신을 호출하는 함수**



### 0. 재귀 함수

 - 특징
    - 작성시 반드시 `base case`가 존재해야 함
       - `base case` 란 점차 범위가 줄어들어 더이상 반복되지 않아 최종적으로 도달하는 곳
   - 알고리즘 구현시 많이 활용
- 장/단점
  - 장점 : 코드가 직관적이고 이해하기 쉬운 경우가 있음
  - 단점 : 함수가 호출될 때마다 메모리 공간에 쌓이므로, Stack Overflow 현상이 발생하거나 프로그램 실행 속도가 늘어짐

- 최대 재귀 깊이 (maximum recursion depth)
  - 재귀함수를 계속적으로 호출하다 보면 RecursionError 가 발생한다.
  - 파이썬에서는 최대 재귀 깊이가 **1,000** 으로 정해져 있다



### 1. 팩토리얼 (factorial)

- **팩토리얼**이란?
  - 1부터 n까지 양의 정수를 차례로 곱한 값
  - **`!`** 기호로 표기
  - `5!` = `5 x 4 x 3 x 2 x1 = 120`
  - 

```python
# recursive function 을 활용한 팩토리얼 함수 구현
def factorial(n):
    # base case
    if n == 1:
        return 1
    # 재귀함수 활용
    return n * factorial(n-1)
```

```python
# while 문을 활용한 팩토리얼 함수 구현
def fact(n):
    # 초기값 설정
    result = 1
    
    # 반복문 실행 - result에 n을 곱하고 n을 1씩 감소시킨다.
    while n > 1:
    	result *= n
        n -= 1
	
    # result 값 반환
    return result
```



### 2. 피보나치 수열

- 피보나치 수열이란?
  - 첫째, 둘째 항이 1이고 그 뒤의 모든 항은 바로 앞 두항의 합인 수열
  - `F0 = F1 = 1`,  `F(n) = F(n-1) + F(n-2)`

```python
# recursive function 을 활용한 함수 구현
def fib(n):
    # n=0, 1 일때
    if n < 2:
        return n
    # 재귀 함수
    else:
        return fib(n-1) + fib(n-2)
```

```python
# 반복문을 활용한 함수 구현
def fib_loop(n):
    # n=0, 1 일때
    if n < 2:
        return n
    
    # n=0, 1 일때의 값을 result 변수에 저장
    result = [0, 1]
    
    # 반복문
    for i in range(2, n+1):
        temp = result[i-2] + result[i-1]
        result.append(temp)
        
    return result
```

