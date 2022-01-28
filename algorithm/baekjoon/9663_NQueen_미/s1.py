import sys
sys.stdin = open('input.txt')

def dfs(queen, row):
    global cnt, N

    if row == N:
        cnt += 1
        return

    for i in range(N):
        queen[row] = i

        for j in range(row):
            if queen[row] == queen[j] or abs(queen[row] - queen[j]) == abs(row - j):
                break
        else:
            dfs(queen, row+1)

N = int(input())

cnt = 0

queens = [0] * N
dfs(queens, 0)

print(cnt)