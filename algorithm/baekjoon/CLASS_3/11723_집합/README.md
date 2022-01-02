# Algorithm | 백준 11723.집합 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 1172.집합 링크](https://www.acmicpc.net/problem/11723)

</br>

#### 문제

비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

- `add x`: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
- `remove x`: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
- `check x`: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
- `toggle x`: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
- `all`: S를 {1, 2, ..., 20} 으로 바꾼다.
- `empty`: S를 공집합으로 바꾼다. 

</br>

#### 입력

첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

</br>

#### 출력

`check` 연산이 주어질때마다, 결과를 출력한다.

#### 코드

</br>

```python
import sys

M = int(input())

S = set()
for _ in range(M):
    lst = sys.stdin.readline().strip().split()
    if len(lst) == 1:
        oper = lst[0]
        if oper == 'all':
            S = set([i for i in range(1, 21)])
        elif oper == 'empty':
            S = set()
    else:
        oper, x = lst[0], lst[1]
        x = int(x)
        if oper == 'add':
            S.add(x)
        elif oper == 'remove':
            S.discard(x)
        elif oper == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif oper == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
```

</br>

#### 풀이

```python
세트 set 자료구조를 사용한다.
'시간초과' 오류를 해결하기 위해 input() 대신 sys.stdin.readline() 코드를 사용하고, 입력받은 연산의 길이가 1이면 all or empty 연산으로 코드를 진행하고 1이 아니라면 add, remove, check, toggle 연산에 대한 코드가 수행된다.

set() 자료구조에서 추가하는 메소드는 .add() 이다.
set() 자료구조에서 제거하는 메소드는 .remove() 와 .discard() 2가지가 있다.
.remove()는 제거하고자 하는 값이 세트 내에 없으면 오류를 반환하고, .discard() 메소드는 제거하려는 값이 세트 내에 없어도 오류가 발생하지 않는다. 따라서 본 문제에서는 .discard() 메소드를 사용하였다.
```



#### 참고

https://mong9data.tistory.com/91

https://yoonsang-it.tistory.com/38



✨ 메모리 초과 이슈가 계속 발생하였다. 단순히 배열을 활용하는 것보다 set() 자료구조와 관련된 메소드를 활용하여 문제를 쉽게 풀 수 있었다. 2022.01.02

