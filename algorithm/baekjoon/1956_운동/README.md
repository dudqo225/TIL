# Algorithm | 백준 1956.운동 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 1956.운동 링크](https://www.acmicpc.net/problem/1956)

</br>

#### 문제

V개의 마을와 E개의 도로로 구성되어 있는 도시가 있다. 도로는 마을과 마을 사이에 놓여 있으며, 일방 통행 도로이다. 마을에는 편의상 1번부터 V번까지 번호가 매겨져 있다고 하자.

당신은 도로를 따라 운동을 하기 위한 경로를 찾으려고 한다. 운동을 한 후에는 다시 시작점으로 돌아오는 것이 좋기 때문에, 우리는 사이클을 찾기를 원한다. 단, 당신은 운동을 매우 귀찮아하므로, 사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.

도로의 정보가 주어졌을 때, 도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오. 두 마을을 왕복하는 경우도 사이클에 포함됨에 주의한다.

</br>

#### 입력

첫째 줄에 V와 E가 빈칸을 사이에 두고 주어진다. (2 ≤ V ≤ 400, 0 ≤ E ≤ V(V-1)) 다음 E개의 줄에는 각각 세 개의 정수 a, b, c가 주어진다. a번 마을에서 b번 마을로 가는 거리가 c인 도로가 있다는 의미이다. (a → b임에 주의) 거리는 10,000 이하의 자연수이다. (a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.

</br>

#### 출력

첫째 줄에 최소 사이클의 도로 길이의 합을 출력한다. 운동 경로를 찾는 것이 불가능한 경우에는 -1을 출력한다.

</br>

#### 코드

```python
import sys

V, E = map(int, input().split())

INF = sys.maxsize
arr = [[INF] * V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

ans = INF
for i in range(V):
    ans = min(ans, arr[i][i])

if ans == INF:
    print(-1)
else:
    print(ans)
```

</br>

#### 풀이

- **플로이드 워셜 알고리즘**을 사용해야 한다.
  - 플로이드 워셜 알고리즘이란?
    - 모든 정점에 관한 최단 경로를 구하는 알고리즘
    - `i → j` 로 가는 경로는 `i → j` 로 바로 가거나, `i → k → j` 와 같이 `k` 정점을 거쳐서 가거나 둘 중 하나이다.

- 알고리즘 구현 순서는 다음과 같다.
  1. 삼중 `for` 반복문 수행
  2. 거쳐가는 정점 `k`를 첫번째 반복문으로 한다.
  3. 삼중 반복문이 종료되고 나서, `arr[i][i]` 값이 `i → i` 로 돌아오는 사이클 경로의 최소값이다.

</br>

#### 참고

- https://yuuj.tistory.com/61
- https://pacific-ocean.tistory.com/280
- https://claude-u.tistory.com/335
- https://tooo1.tistory.com/312

</br>

플로이드 워셜 알고리즘 자체를 모르면 절대 못풀 것 같다. 이런식으로 특정 알고리즘을 숙지한 상태에서 풀어야 하는 문제들이 꽤 있다. 😅
