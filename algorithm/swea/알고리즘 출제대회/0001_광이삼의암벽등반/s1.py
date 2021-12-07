import sys
sys.stdin = open('input.txt')

def solve(x, y, cnt):
    global M, N, L, mat, visited, ans

    if mat[x][y] == 3:
        ans = cnt - 1

    for i in range(x, M):
        for j in range(y, N):
            if not visited[i][j] and (mat[i][j] == 1 or mat[i][j] == 3) and abs(x-i) + abs(y-j) <= L:
                visited[i][j] = 1
                solve(i, j, cnt+1)
                visited[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    M, N, L = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(M)]

    visited = [[0] * N for _ in range(M)]


    ans = -1
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 2:
                ans = solve(i, j, 0)

    print(ans)