# Algorithm | 백준 1406.에디터 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 1406.에디터 링크](https://www.acmicpc.net/problem/1406)

</br>

#### 문제

한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.

이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

이 편집기가 지원하는 명령어는 다음과 같다.

| L    | 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)  |
| :--- | ------------------------------------------------------------ |
| D    | 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨) |
| B    | 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨) 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임 |
| P $  | $라는 문자를 커서 왼쪽에 추가함                              |

초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

</br>

#### 입력

첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다. 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다. 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다. 명령어는 위의 네 가지 중 하나의 형태로만 주어진다.

</br>

#### 출력

첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.

</br>

#### 코드

##### s1.py

```python
import sys

words = sys.stdin.readline().rstrip()
N = len(words)
M = int(input())

for _ in range(M):
    command = list(sys.stdin.readline().split())

    if command[0] == 'P':
        words = words[:N] + command[1] + words[N:]
        N += 1
    elif command[0] == 'L':
        if N != 0:
            N -= 1
    elif command[0] == 'D':
        if N != len(words):
            N += 1
    elif command[0] == 'B':
        if N != 0:
            words = words[:N-1] + words[N:]
            N -= 1

print(words)
```

- 입력받는 단어의 길이 N을 커서로 정해서, 리스트 슬라이싱 방법을 사용하여 커맨드에 따라서 문자를 조정하였다.
- 하지만 결과는 '시간초과'...

</br>

##### s2.py

```python
import sys
from collections import deque

words = deque(sys.stdin.readline().rstrip())
N = len(words)
M = int(input())

words2 = deque()

for _ in range(M):
    command = list(sys.stdin.readline().split())

    if command[0] == 'P':
        words.append(command[1])
    elif command[0] == 'L' and words:
        words2.appendleft(words.pop())
    elif command[0] == 'D' and words2:
        words.append(words2.popleft())
    elif command[0] == 'B' and words:
        words.pop()

print(''.join(words + words2))
```

</br>

#### 풀이

```python
"시간초과" 문제를 해결하기 위해 파이썬 내장 collections의 deque를 사용하였다.
기존 입력받은 문자열을 words에 저장하고, 비어있는 deque를 words2 이름으로 새롭게 생성한다.

1. 커맨드가 P일 때 : 기존 words에 문자를 추가
2. 커맨드가 L일 때 : words의 마지막 문자를 떼어서 words2 앞에 붙인다.
3. 커맨드가 D일 때 : words2의 첫번째 문자를 떼어서 words 마지막에 붙인다.
4. 커맨드가 B일 때 : words의 마지막 문자를 삭제한다.

처음에는 커서를 기준으로 해서 인덱스 조정을 했는데, 구글링을 해서 다른 사람들의 풀이 코드를 보니 스택 or 큐 자료구조를 활용해서 커서의 역할을 대신하는 풀이가 많았다. 커맨드에 따라서 2개의 deque에 문자열을 저장하고 모든 커맨드 연산이 끝난 후에, .join() 메소드로 결과를 출력했다.
```

</br>

#### 참고

https://bnzn2426.tistory.com/112

https://velog.io/@gothae/1406-python



✨ 세상에 참 똑똑한 사람이 많다. 2022.01.09
