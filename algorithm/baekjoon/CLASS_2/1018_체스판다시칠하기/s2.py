import sys
sys.stdin = open('input.txt')

def check(arr):

    cnt = 0

    i, j = 0, 0
    current = arr[0][0]

    while i < N:

        if current != arr[i][j]:
            cnt += 1
        if current == 'W':
            current = 'B'
        else:
            current = 'W'

        print(i, j, current)
        if j == M-1:
            i += 1
            j = 0
            continue
        j += 1

    return cnt

# 세로, 가로
N, M = map(int, input().split())

chess = [[i for i in input()] for _ in range(N)]

ans = 9876543210

res = check(chess)

print(res)