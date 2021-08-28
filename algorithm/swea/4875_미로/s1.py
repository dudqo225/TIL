import sys
sys.stdin = open('input.txt')

# 미로에서 출발지 → 도착지 경로가 존재하는지 확인하는 함수 생성
def checkMaze():
    # 전역 변수 불러오기
    global mat, visited, s_i, s_j, e_i, e_j

    # x축, y축 델타 리스트 생성
    dx = [0, 1, 0, -1] # 우 하 좌 상
    dy = [1, 0, -1, 0] # 우 하 좌 상

    # 스택에 출발지 i, j 인덱스 삽입
    stack = [[s_i, s_j]]

    # 스택이 빌 때까지 반복
    while stack:
        # 스택의 마지막 값을 pop해서 v에 저장
        v = stack.pop()
        # v에 방문한 것으로 표시
        visited[v[0]][v[1]] = 1
    
        # v가 도착지라면, 1을 리턴
        if v == [e_i, e_j]:
            return 1
        
        # 우 하 좌 상 탐색을 위해 0~3까지 반복
        for k in range(4):
            w_i = v[0] + dx[k]
            w_j = v[1] + dy[k]
            # 현 위치에 델타값을 더한 값이 미로 범위 안에 있고, 벽이 아니면서 아직 방문하지 않았다면
            if w_i in range(N) and w_j in range(N) and mat[w_i][w_j] != 1 and visited[w_i][w_j] == 0:
                # 스택에 추가하고, 방문한 것으로 표시
                stack.append([w_i, w_j])
                visited[w_i][w_j] = 1

    # 스택이 비어질 때까지 도착지를 찾지 못하면 미로를 탈출할 수 있는 경로가 없는 것이므로 0을 리턴
    return 0

# 테스트 케이스 개수 T 입력
T = int(input())
for tc in range(1, T+1):
    # 행렬 크기 N 입력
    N = int(input())

    # NxN 행렬 입력
    mat = [list(map(int, input())) for _ in range(N)]
    # 방문 여부 체크를 위한 NxN 행렬 생성
    visited = [[0 for _ in range(N)] for _ in range(N)]

    # 출발점, 도착점 인덱스 찾기
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                s_i = i
                s_j = j
            if mat[i][j] == 3:
                e_i = i
                e_j = j
    
    # checkMaze 함수 결과를 ans에 저장
    ans = checkMaze()
    
    # 결과 출력
    print('#{} {}'.format(tc, ans))