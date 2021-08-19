import sys
sys.stdin = open('input.txt')

def dfs():
    global V, E, graph, visited, S, G

    stack = [S]

    while len(stack) > 0:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1

            for w in range(1, V+1):
                if graph[v][w] == 1 and visited[w] == 0:
                    stack.append(w)

    if visited[G] == 1:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph_list = [list(map(int, input().split())) for _ in range(E)]

    S, G = map(int, input().split())

    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for i in range(E):
        start = graph_list[i][0]
        end = graph_list[i][1]

        graph[start][end] = 1

    print('#{} {}'.format(tc, dfs()))