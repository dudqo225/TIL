import sys
sys.stdin = open('input.txt')

def check(arr):

    cnt = 0
    if arr[0][0] == 'B':
        for i in range(N):
            for j in range(M//2):
                if arr[i][2*j] != 'B':
                    cnt += 1
                if arr[i][2*j+1] != 'W':
                    cnt += 1
    else:
        for i in range(N):
            for j in range(M//2):
                if arr[i][2*j] != 'W':
                    cnt += 1
                if arr[i][2*j+1] != 'B':
                    cnt += 1

    return cnt

# 세로, 가로
N, M = map(int, input().split())

chess = [[i for i in input()] for _ in range(N)]

ans = 9876543210

res = check(chess)

print(res)