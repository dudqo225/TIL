# Algorithm | 백준 17086.아기 상어 2 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 17086.아기 상어 2 링크](https://www.acmicpc.net/problem/17086)

</br>

#### 문제

N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.

어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

안전 거리가 가장 큰 칸을 구해보자. 

</br>

#### 입력

첫째 줄에 공간의 크기 N과 M(2 ≤ N, M ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에 공간의 상태가 주어지며, 0은 빈 칸, 1은 아기 상어가 있는 칸이다. 빈 칸의 개수가 한 개 이상인 입력만 주어진다.

</br>

#### 출력

첫째 줄에 안전 거리의 최댓값을 출력한다.

</br>

#### 코드

```python
from collections import deque


# bfs 함수 작성
def bfs():
    global ans

    while q:
        x, y = q.popleft()
        # 8방향 탐색
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            # nx, ny 좌표가 범위 내에 있으면
            if 0 <= nx < N and 0 <= ny < M:
                if mat[nx][ny] == 0:
                    q.append((nx, ny))
                    mat[nx][ny] = mat[x][y] + 1
                    ans = max(ans, mat[nx][ny])


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

q = deque()

# 아기 상어 좌표 찾기
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            q.append((i, j))

# → 부터 시계방향
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

ans = 0
bfs()

print(ans - 1)
```

</br>

#### 풀이

- **BFS** 를 이용하여 문제를 해결하였다.
- `NxM` 크기의 공간을 순회하면서 공간값이 `1` 이면 아기 상어가 존재하므로 `deque()`로 생성한 `q` 에 아기 상어가 존재하는 i,  j 좌표쌍을 넣어준다.
- 이후  `BFS` 함수를 실행한다. `q` 에서 한 쌍씩 꺼내서 인접한 8방향으로 탐색을 진행하고 탐색한 곳의 값이 `0` 이면 상어가 존재하지 않으므로 안전하다. 안전한 곳의 좌표 nx, ny 를 다시 `q`에 넣어주고 그 위치의 값은 기존 좌표값 + 1 해준다. 현재 안전거리의 최댓값과 좌표값을 비교하여 `ans` 에 할당한다.
