import sys
sys.stdin = open('input.txt')

def dfs(v):
    global adj
    result = []
    stack = [1]
    visited = [0] * (N+1)

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = 1
            result.append(v)
            for w in range(N+1):
                if adj[v][w] and not visited[w]:
                    stack.append(w)

    return result

N = 7
V = 8

adj = [[0] * (N+1) for _ in range(N+1)]

arr = list(map(int, (input().split())))

for i in range(0, len(arr), 2):
    adj[arr[i]][arr[i+1]], adj[arr[i+1]][arr[i]] = 1, 1

print(dfs(1))

