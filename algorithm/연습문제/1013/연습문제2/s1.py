import sys
sys.stdin = open('input.txt')

def bfs(v):
    global adj

    result = []

    que = [v]
    visited = [0] * (N+1)

    while que:
        v = que.pop(0)
        if not visited[v]:
            visited[v] = 1
            result.append(v)

            for w in range(N+1):
                if adj[v][w] and not visited[w]:
                    que.append(w)

    return result

N = 7
V = 8

arr = list(map(int, input().split()))

adj = [[0] * (N+1) for _ in range(N+1)]

for i in range(0, len(arr), 2):
    adj[arr[i]][arr[i+1]], adj[arr[i+1]][arr[i]] = 1, 1

print(bfs(1))