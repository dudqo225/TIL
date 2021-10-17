import sys

sys.stdin = open('input.txt')


def dfs(X):
    global adj, visited

    visited[X] = 1
    print(X, end=' ')

    for i in range(1, N + 1):
        if not visited[i] and adj[X][i]:
            dfs(i)


def bfs(X):
    global adj

    visited = [0] * (N + 1)
    que = [X]
    visited[X] = 1
    print(X, end=' ')
    while que:
        tmp = que.pop(0)

        for i in range(N + 1):
            if not visited[i] and adj[tmp][i]:
                visited[i] = 1
                print(i, end=' ')
                que.append(i)


N, M, V = map(int, input().split())

adj = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())

    adj[a][b] = adj[b][a] = 1

visited = [0] * (N + 1)
ans1 = dfs(V)
print()
ans2 = bfs(V)