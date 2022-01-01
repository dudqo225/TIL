import sys
sys.stdin = open('input.txt')

N, M, B = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * 257

for i in range(N):
    for j in range(M):
        height = ground[i][j]
        visited[height] += 1

obj = visited.index(max(visited))

ans = 0

for i in range(N):
    for j in range(M):
        if ground[i][j] < obj:
            B -= obj - ground[i][j]
            ground[i][j] += obj - ground[i][j]
            ans += 1
        elif ground[i][j] > obj:
            B += ground[i][j] - obj
            ground[i][j] -= ground[i][j] - obj
            ans += 2

print(ans, obj)