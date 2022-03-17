# Algorithm | 백준 2667.단지번호붙이기 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 2667.단지번호붙이기 링크](https://www.acmicpc.net/problem/2667)

</br>

#### 문제

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

![img](images/ITVH9w1Gf6eCRdThfkegBUSOKd-16475049180372.png) 

</br>

#### 입력

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

</br>

#### 출력

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

</br>

#### 코드

```python
def dfs(x, y):
    global arr, cnt, dx, dy

    arr[x][y] = 0
    cnt += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny]:
            dfs(nx, ny)


N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

blocks = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i, j)
            blocks.append(cnt)

blocks.sort()
print(len(blocks))
for block in blocks:
    print(block)
```

</br>

#### 풀이

- **DFS** 를 이용하여 문제를 해결하였다.
- `NxN` 크기의 단지를 입력하고 이중반복문을 돌면서 `1`(집이 있는 곳)인 경우 `dfs(i, j)` 함수를 시행한다.
- `dfs(i, j)` 함수는 4방향 탐색을 하고, 내부적으로 `dfs()` 함수를 수행하는 재귀 구조를 띄고 있다.
- **전체적으로 한 번의 `dfs(i, j)` 함수를 수행하고 종료되는 것 = 하나의 단지를 탐색한 것** 을 의미한다.
  - 이 때 `cnt` 값을 `blocks` 리스트에 추가해준다.
- 모든 탐색이 완료되고 나면, `blocks` 리스트를 정렬하고 출력 방식에 맞게 결과를 출력한다.
