import sys

sys.stdin = open('input.txt')


def dijkstra(s, mat):
    dist = [987654321] * (N + 1)
    visited = [0] * (N + 1)

    dist[s] = 0

    for _ in range(N):
        min_idx = -1
        min_val = 987654321

        # 최소값 찾기
        for i in range(N + 1):
            if not visited[i] and min_val > dist[i]:
                min_idx = i
                min_val = dist[i]

        visited[min_idx] = 1

        # 갱신할수 있으면 갱신
        for i in range(N + 1):
            if not visited[i] and dist[i] > dist[min_idx] + mat[min_idx][i]:
                dist[i] = dist[min_idx] + mat[min_idx][i]

    return dist[1:]


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())

    adj_arr1 = [[987654321] * (N + 1) for _ in range(N + 1)] # 원래입력 (진출)
    adj_arr2 = [[987654321] * (N + 1) for _ in range(N + 1)] # 반대입력 (진입)

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj_arr1[x][y] = c
        adj_arr2[y][x] = c

    max_val = 0

    tmp1 = dijkstra(X, adj_arr1)
    tmp2 = dijkstra(X, adj_arr2)

    for i in range(N):
        if tmp1[i] + tmp2[i] > max_val:
            max_val = tmp1[i] + tmp2[i]

    print('#{} {}'.format(tc, max_val))