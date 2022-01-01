# Algorithm | 백준 1003.피보나치 함수 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 1003.피보나치 함수 링크](https://www.acmicpc.net/problem/1003)

</br>

#### 문제

다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

```
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
```

`fibonacci(3)`을 호출하면 다음과 같은 일이 일어난다.

- `fibonacci(3)`은 `fibonacci(2)`와 `fibonacci(1)` (첫 번째 호출)을 호출한다.
- `fibonacci(2)`는 `fibonacci(1)` (두 번째 호출)과 `fibonacci(0)`을 호출한다.
- 두 번째 호출한 `fibonacci(1)`은 1을 출력하고 1을 리턴한다.
- `fibonacci(0)`은 0을 출력하고, 0을 리턴한다.
- `fibonacci(2)`는 `fibonacci(1)`과 `fibonacci(0)`의 결과를 얻고, 1을 리턴한다.
- 첫 번째 호출한 `fibonacci(1)`은 1을 출력하고, 1을 리턴한다.
- `fibonacci(3)`은 `fibonacci(2)`와 `fibonacci(1)`의 결과를 얻고, 2를 리턴한다.

1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, `fibonacci(N)`을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

</br>

#### 코드

##### s1.py

```python
def fibo(N):
    global zero, one

    if N == 0:
        zero += 1
        return 0
    elif N == 1:
        one += 1
        return 1
    else:
        return fibo(N-1) + fibo(N-2)

T = int(input())
for tc in range(1, T+1):
    number = int(input())

    zero, one = 0, 0

    fibo(number)

    print(zero, one)
```

- 피보나치 함수를 기본적인 재귀방식으로 프로그래밍한 코드이다.
- TC에 대해서 정상적인 답이 나오지만, N이 22를 넘어서면서부터는 실행 시간이 급격히 증가한다.
- 결국 **시간초과** 로 문제 해결 실패

<br>

##### s2.py

```python
def fibo(N):
    global zero, one

    if N > 2:
        for i in range(3, N+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

T = int(input())
for tc in range(1, T+1):
    number = int(input())

    zero = [1, 0, 1]
    one = [0, 1, 1]

    fibo(number)

    print(zero[number], one[number])
```

</br>

#### 풀이

```python
재귀적으로 피보나치 함수를 구현하면 시간초과로 문제 해결에 실패한다.

피보나치 함수는 규칙성이 있기 때문에 1, 0이 호출횟수도 규칙성을 찾아서 구해주면 된다.

fibonacci(3)에서 0과 1의 호출 횟수는 fibonacci(2)와 fibonacci(1)의 0과 1의 호출 횟수의 합과 같다.
fibonacci(4)에서 0과 1의 호출 횟수는 fibonacci(3)와 fibonacci(2)의 0과 1의 호출 횟수의 합과 같다.

이를 공식화 하면,
fibonacci(N)에서의 0과 1의 호출 횟수는 fibonacci(N-1)과 fibonacci(N-2)의 0과 1의 호출 횟수의 합 이다.

따라서 base case인 0과 1 그리고 2까지에 대해서 각각 zero, one 리스트를 미리 만들고
for 문을 반복하면서 위의 공식을 적용한다.

결과는 zero와 one 리스트의 N번째 인덱스 값을 출력한다.
```



#### 참고

https://itstory1592.tistory.com/34

https://doorbw.tistory.com/58



✨ 2022년 새해 첫 알고리즘 문제를 풀었다. 개발 공부를 처음 시작할 때만 해도 피보나치 함수를 간단한 재귀방식으로 구현하는 것도 어려워 했었는데, 이제는 시간 복잡도에 대해서 고민하는 문제를 풀다니... 물론 구글링을 통해서 문제를 해결하긴 했지만 실력이 조금은 성장한 것 같아 뿌듯하다. 올 한해도 열심히 성장하자!!! 2022.01.01

