import sys

sys.stdin = open('input.txt')


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    edges = [list(map(int, input().split())) for _ in range(M)]

    adj = [[0] * (N + 1) for _ in range(N + 1)]

    p = [i for i in range(N + 1)]

    for i in range(M):
        a = edges[i][0]
        b = edges[i][1]

        p[find_set(b)] = find_set(a)

    ans = 0

    # 인덱스와 각 자릿수 값이 일치하면, 그룹을 대표 > 그룹의 수
    for i in range(1, N + 1):
        if p[i] == i:
            ans += 1

    print('#{} {}'.format(tc, ans))
