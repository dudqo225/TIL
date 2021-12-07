import sys
sys.stdin = open('input.txt')

def solve(j):
    global y, ans
    ans += abs(j-y) + 1

T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(R)]

    ans = 1
    x, y = 0, 0
    gorae = False
    while x < R:
        if 1 not in mat[x]:
            break
        for j in range(C):
            if mat[x-1][j] == 2:
                gorae = True
                break
            if mat[x][j] == 1:
                solve(j)
                y = j
        if gorae == True:
            break
        x += 1

    print('#{} {}'.format(tc, ans))