import sys
sys.stdin = open('input.txt')

def mazeCount():
    global maze, s_x, s_y, e_x, e_y, visited

    que = [[s_x, s_y]] # 시작점을 que에 넣는다.
    dx = [0, 1, 0, -1] # 우 하 좌 상
    dy = [1, 0, -1, 0]

    # que가 빌 때까지 반복
    while que:
        # v 는 현 위치
        v = que.pop(0)
        # 현 위치가 도착점이라면, 함수 종료
        if v == [e_x, e_y]:
            result = visited[e_x][e_y] - 1
            return result
        # 델타 리스트를 활용해서 4방 탐색
        for k in range(4):
            ci = v[0] + dx[k]
            cj = v[1] + dy[k]
            # ci, cj가 범위 안에 있고 벽이 아니면서 아직 방문하지 않았을 경우
            if ci in range(N) and cj in range(N) and maze[ci][cj] != 1 and not visited[ci][cj]:
                # ci, cj를 que에 추가하고 지나온 길은 2(임의의 수)로 변경
                que.append([ci, cj])
                maze[ci][cj] = 2
                # 직전의 지나온 칸 수 +1을 ci, cj의 지나온 칸 수에 저장
                visited[ci][cj] = visited[v[0]][v[1]] + 1

    # 경로가 없으면 0을 리턴
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [[0 for _ in range(N)] for _ in range(N)]
    # 미로 리스트 그리기
    for i in range(N):
        arr = input()
        for j in range(N):
            maze[i][j] = int(arr[j])
            # 출발점, 도착점 인덱스 찾기
            if maze[i][j] == 2:
                # 출발점 x, y 좌표
                s_x = i
                s_y = j
            if maze[i][j] == 3:
                # 도착점 x, y 좌표
                e_x = i
                e_y = j

    visited = [[0 for _ in range(N)] for _ in range(N)]
    print('#{} {}'.format(tc, mazeCount()))
