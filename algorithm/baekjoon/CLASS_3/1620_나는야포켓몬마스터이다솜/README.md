# Algorithm | 백준 1620.나는야 포켓몬 마스터 이다솜 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 1620.나는야 포켓몬 마스터 이다솜 링크](https://www.acmicpc.net/problem/1620)

</br>

#### 문제

문제 지문이 상당히 길다. 문제 내용은 상단 링크를 통해 확인하자.

</br>

#### 입력

첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져. N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수인데, 자연수가 뭔지는 알지? 모르면 물어봐도 괜찮아. 나는 언제든지 질문에 답해줄 준비가 되어있어.

둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와. 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어. 아참! 일부 포켓몬은 마지막 문자만 대문자일 수도 있어. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야. 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와. 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅!!!

#### 코드

##### s1.py

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pocketmon_book = [0]

for _ in range(N):
    pocketmon = input().rstrip()
    pocketmon_book.append(pocketmon)

for i in range(M):
    val = input().rstrip()
    if val.isalpha():
        print(pocketmon_book.index(val))
    else:
        print(pocketmon_book[int(val)])
```

- **시간초과** 로 문제 해결 실패. 기본 `input()` 대신, `sys.stdin.readline` 을 활용하였으나 이것 외에도 다른 부분에서 시간초과가 발생한 듯 하다.
- `.index()` 를 사용해서 그런 것 같다

<br>

##### s2.py

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pocketmon_list = []
pocketmon_dict = {}

for i in range(N):
    pocketmon = input().rstrip()
    pocketmon_list.append(pocketmon)
    pocketmon_dict[pocketmon] = i+1

for i in range(M):
    val = input().rstrip()
    if val.isalpha():
        print(pocketmon_dict[val])
    else:
        print(pocketmon_list[int(val)-1])
```

</br>

#### 풀이

```python
.index()를 사용하면 시간초과가 발생하기 때문에, 딕셔너리 자료구조를 활용하여 키-값 쌍에서 쉽게 값을 활용하여 각 포켓몬에 알맞은 도감 번호를 찾으면 해결.

1. pocketmon_list에는 포켓몬 이름을 저장한다.
2. pocketmon_dict에는 포켓몬 이름을 키(key)로, i+1을 값(value)로 하여 저장한다.
3. 입력값 val이 알파벳인지 확인하는 .isalpha() 메소드를 사용하여 알파벳이라면 pocketmon_dict에서 val에 해당하는 값을 출력하고, 숫자라면 pocketmon_list에서 int(val)-1 번째 인덱스의 포켓몬 이름을 출력한다.

문제의 핵심은 파이썬 내장 메소드를 사용하여 시간초과 문제가 나오는 것을 딕셔너리 자료구조를 사용함으로써 해결하는 것이다. 문제의 지문이 긴 것에 비해 풀이 과정은 그렇게 어렵지는 않았다. 하지만 항상 모든 알고리즘 문제를 풀면서 마주치는 오류. *시간초과* 를 해결하는 여러가지 방법에 대해서 꾸준히 연습할 필요가 있다.
```



#### 참고

https://seraup.dev/10

https://gudwns1243.tistory.com/63

https://claude-u.tistory.com/264



✨ 포켓몬이라는 주제가 참신하고 친숙하여 문제를 재밌게 풀 수 있었다. 파이썬 내장 메소드가 아닌 자료구조를 활용하여 시간 복잡도 문제를 해결하는 과정이 매우 유익했다. 2022.01.01

