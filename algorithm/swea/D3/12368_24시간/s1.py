import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())

    if A + B < 24:
        ans = A + B
    elif A + B == 24:
        ans = 0
    elif A + B > 24:
        ans = A + B - 24

    print('#{} {}'.format(tc, ans))