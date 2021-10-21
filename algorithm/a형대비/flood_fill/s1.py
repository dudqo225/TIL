def bfs(i, j, level):
    global map, visited

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = [(i, j, level)]
    visited[i][j] = 1

    while queue:
        x, y, l = queue.pop(0)

        # print(x, y, l)
        if x == 0 and y == 4:
            return l

        for w in range(4):
            nx = x + dx[w]
            ny = y + dy[w]

            if 0 <= nx < 4 and 0 <= ny < 5 and not visited[nx][ny] and map[nx][ny] != 1:
                visited[nx][ny] = 1
                queue.append((nx, ny, l+1))


map = [
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

visited = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


print(bfs(0, 0, 0))