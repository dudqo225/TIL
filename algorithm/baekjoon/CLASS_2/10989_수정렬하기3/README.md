# Algorithm | 백준 10989.수 정렬하기 3 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 10989.수 정렬하기 3 링크](https://www.acmicpc.net/problem/10989)

</br>

#### 문제

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

</br>

#### 코드

```python
import sys

N = int(input())

check = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())

    check[num] += 1

for i in range(10001):
    if check[i] != 0:
        for j in range(check[i]):
            print(i)
```

</br>

#### 풀이

```python
이 문제는 '시간초과' 와 '메모리초과' 두 가지를 모두 고려해야 하는 어려운 문제이다. 단순한 수 정렬 문제라고 생각해서 .sort() 나 sorted()를 사용하면 틀린다.

1. '시간초과' 오류는 백준 문제에서 자주 접하게 되는 상황이다. 이때마다 구글링을 통해 찾아보는 대부분의 글에서 단순 input() 대신 import sys > sys.stdin.readline() 을 사용할 것을 말해준다.

2. '메모리초과' 는 for문에서 .append() 메서드를 사용하면 메모리 재할당이 이루어져 발생하는 문제이다. 입력값이 크지 않을 때에는 큰 문제가 되지 않으나 입력값이 극한으로 많은 문제에서는 메모리를 효율적으로 사용해야 문제를 해결할 수 있다.
 메모리초과 문제를 해결하기 위해 [0] 으로 이루어진 길이가 10001인 리스트(check)를 만든다. 입력값을 받을 때마다 해당 입력값을 인덱스로 하여 check 리스트에 1씩 더해준다.
 N번의 입력을 다 받고난 후, check를 순회하면서 check의 i번째 인덱스를 그 값 횟수만큼 반복 출력한다.
```



#### 참고

https://yoonsang-it.tistory.com/49

https://somjang.tistory.com/entry/Mxmxmxm



✨ 시간복잡도와 공간복잡도 두 가지를 모두 고려해야 하는 다소 난해한 문제였다. '풀이'에 서술하였듯 시간복잡도는 sys.stdin.readline()으로 해결하고, 공간복잡도는 단순 .append() 대신 check 리스트를 만들어 메모리 재할당을 줄여 문제를 해결한다. 2021.12.26

