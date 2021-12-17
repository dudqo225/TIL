import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    A, B, C, D = map(int, input().split(' '))

    start = max(A, C)
    end = min(B, D)

    if end - start < 0:
        ans = 0
    else:
        ans = end - start

    print('#{} {}'.format(tc, ans))