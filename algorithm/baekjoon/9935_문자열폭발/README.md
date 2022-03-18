# Algorithm | 백준 9935.문자열 폭발 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 9935.문자열 폭발 링크](https://www.acmicpc.net/problem/9935)

</br>

#### 문제

상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

폭발은 다음과 같은 과정으로 진행된다.

- 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
- 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
- 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.

상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.

폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.

</br>

#### 입력

첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.

둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.

두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.

</br>

#### 출력

첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.

</br>

#### 코드

##### s1.py

- 채점 중 `47%` 지점에서 **시간초과** 로 문제 풀이 실패
- 파이썬 내장 메소드인 `.replace()` 를 써서 시간 초과가 나는 듯 하다.

```python
import sys

words = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

while True:
    if bomb in words:
        words = words.replace(bomb, '')
    else:
        break

if words:
    print(words)
else:
    print("FRULA")

```

</br>

##### s2.py

```python
import sys

words = sys.stdin.readline().rstrip()
bomb = list(sys.stdin.readline().rstrip())

stack = []

for word in words:
    stack.append(word)
    if stack[-1] == bomb[-1] and stack[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
```

</br>

#### 풀이

- **Stack** 구조를 이용하여, 리스트에 차곡차곡 쌓아가면서 폭발 문자열일 때 삭제해주는 방식으로 문제를 풀었다.
  - `words` 변수를 반복문으로 순회하면서 모든 `word`를 `stack` 리스트에 추가
  - `stack` 의 마지막 원소와 폭발 문자열(`bomb`)의 마지막 원소가 일치하고
  - `stack`의 마지막 원소들(폭발 문자열의 길이만큼)과 폭발 문자열이 일치하는 경우
  - 폭발 문자열의 길이만큼  `stack` 에서 제거한다.
- 출력을 할 때에는 `.join()` 메소드를 사용하여 리스트 안에 있는 데이터를 하나의 문자열로 이어서 출력했다.

</br>

알고리즘에서 `.replace()` 같은 내장 함수를 쓰면 거의 문제가 해결이 안되는 것 같다. 시간초과...🤣

각 문제에 맞는 적절한 **알고리즘**과 **자료구조**를 사용하는 것이 중요하다.

