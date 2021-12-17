import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, R = map(int, input().split())

    child = 1
    for i in range(N, N-R, -1):
        child *= i

    parent = 1
    for i in range(R, 0, -1):
        parent *= i

    value = child // parent
    ans = value % 1234567891

    print('#{} {}'.format(tc, ans))