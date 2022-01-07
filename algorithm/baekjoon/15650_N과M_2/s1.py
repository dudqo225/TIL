import sys
sys.stdin = open('input.txt')

def dfs(start, depth):
    if depth == M:
        print(*s)
        return

    for i in range(start, N+1):
        if not visited[i]:
            visited[i] = 1
            s.append(i)
            dfs(i+1, depth+1)
            s.pop()
            visited[i] = 0

N, M = map(int, input().split())

visited = [0] * (N+1)
s = []
dfs(1, 0)