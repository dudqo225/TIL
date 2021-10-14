import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs():
    global ans

    while q:
        num, cnt = q.popleft()
        if num == e:
            ans = cnt
            return

        # +1, -1, *2, -10
        for i in range(4):
            if i == 0:
                if 1 <= num + 1 <= 1000000 and not visited[num + 1]:
                    q.append([num + 1, cnt + 1])
                    visited[num + 1] = 1
            elif i == 1:
                if 1 <= num - 1 <= 1000000 and not visited[num - 1]:
                    q.append([num - 1, cnt + 1])
                    visited[num - 1] = 1
            elif i == 2:
                if 1 <= num * 2 <= 1000000 and not visited[num * 2]:
                    q.append([num * 2, cnt + 1])
                    visited[num * 2] = 1
            elif i == 3:
                if 1 <= num - 10 <= 1000000 and not visited[num - 10]:
                    q.append([num - 10, cnt + 1])
                    visited[num - 10] = 1

T = int(input())
for tc in range(1, T + 1):
    s, e = map(int, input().split())

    ans = 0
    visited = [0] * 1000001

    q = deque()
    q.append([s, 0])

    bfs()

    print('#{} {}'.format(tc, ans))