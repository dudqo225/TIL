import sys
sys.stdin = open('input.txt')

def check(idx):
    global total, ans, checked, mat

    if ans > total:
        return

    if idx == N:
        if ans < total:
            total = ans
            return
    for i in range(N):
        if checked[i] == 0:
            checked[i] = 1
            ans += mat[idx][i]
            check(idx+1)
            checked[i] = 0
            ans -= mat[idx][i]

    return total

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    checked = [0] * N

    ans = 0
    idx = 0
    total = 9876543210

    print('#{} {}'.format(tc, check(0)))