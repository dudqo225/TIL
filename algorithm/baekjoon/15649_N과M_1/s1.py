import sys
sys.stdin = open('input.txt')

def dfs(l):
    global visited, arr

    if l == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if visited[i]:
           continue

        visited[i] = 1
        arr.append(i)
        dfs(l+1)
        arr.pop()
        visited[i] = 0

N, M = map(int, input().split())

visited = [0] * (N+1)
arr = []
dfs(0)