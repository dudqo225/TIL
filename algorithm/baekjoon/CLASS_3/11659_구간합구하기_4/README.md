# Algorithm | 백준 11659.구간 합 구하기 4 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 11659.구간 합 구하기 4 링크](https://www.acmicpc.net/problem/11659)

</br>

#### 문제

수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

</br>

#### 입력

첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

</br>

#### 출력

총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

</br>

#### 제한

- 1 ≤ N ≤ 100,000
- 1 ≤ M ≤ 100,000
- 1 ≤ i ≤ j ≤ N

</br>

#### 코드

```python
import sys

N, M = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

accumulate_lst = [0]
total = 0
for number in numbers:
    total += number
    accumulate_lst.append(total)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    ans = accumulate_lst[j] - accumulate_lst[i-1]
    print(ans)
```

</br>

#### 풀이

```python
N개의 숫자가 나열되어 있을 때 특정 구간의 수를 합한 값을 구하는 문제이다.
i~j까지 구간이 주어지는데, i부터 j까지 반복하면서 구간의 합을 구하면 시간복잡도 문제를 해결할 수 없다.
본 문제에서도 N과 M의 최대 100,000으로 주어지는데 최악의 경우 O(NM)의 시간 복잡도를 가진다.

따라서 미리 각 구간의 합을 저장하는 리스트를 만들어두고, 구간에 따른 합을 구하면 시간 복잡도 문제를 해결할 수 있다.

구간합을 저장하는 리스트 accumulate_lst = [0] 으로 초기화하고, 구간합 total 변수를 0으로 초기화한다.
입력받은 N개의 숫자 리스트 numbers를 순회하면서 total 변수에 더해주고, 각 구간합을 accumulate_lst에 추가한다.

구간 합 계산은 i를 시작값, j를 종료값으로 했을 때
accumulate_lst[j] - accumulate_lst[i-1]
로 계산할 수 있다.
```

</br>

#### 참고

https://velog.io/@koyo/python-prefix-sum

https://velog.io/@kimdukbae/BOJ-11659-%EA%B5%AC%EA%B0%84-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-4-Python



✨ 알고리즘 수업을 들을 때도 그렇고, 요즘 혼자서 알고리즘 문제를 풀 때도 그렇고, 너무 어렵다. 기본적인 배경지식과 더불어 문제를 이해하고 코드로 구현하는 능력이 다 필요한 것 같은데, 왜 난 다 없는것 같지..🤣 2022.01.09
