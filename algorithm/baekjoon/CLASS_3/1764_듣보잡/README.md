# Algorithm | 백준 1764.듣보잡 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 1764.듣보잡 링크](https://www.acmicpc.net/problem/1764)

</br>

#### 문제

김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

</br>

#### 입력

첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

</br>

#### 출력

듣보잡의 수와 그 명단을 사전순으로 출력한다.

#### 코드

</br>

```python
import sys

N, M = map(int, sys.stdin.readline().split())

person_dict = {}

for _ in range(N):
    person = sys.stdin.readline().rstrip()
    person_dict[person] = 1

ans = []

for _ in range(M):
    person = sys.stdin.readline().rstrip()

    if person in person_dict.keys():
        ans.append(person)

ans.sort()

print(len(ans))
print('\n'.join(ans))
```

</br>

#### 풀이

```python
딕셔너리 자료구조를 활용하여 N명의 듣도 못한 사람을 저장한다. M명의 보도 못한 사람을 확인할 때, .keys() 메소드를 사용하여 이미 존재하는 키값이라면 듣도 보도 못한 사람으로 규정할 수 있으므로 ans 리스트에 추가해준다. 사전순으로 출력해야 하기 때문에 파이썬 내장 .sort()로 정렬해주고 결과를 출력한다.

결과 출력은 먼저 len(ans)로 듣보잡의 수를 출력하고, .join() 메서드로 명단을 출력해준다.
```



#### 참고



✨ 어제에 이어서 딕셔너리 자료구조를 활용하여 문제를 해결하였다. P.S 해결에서는 단순 배열/리스트 외에도 다양한 자료구조를 통해서 문제를 해결할 수 있음을 명심하자. 2022.01.02

