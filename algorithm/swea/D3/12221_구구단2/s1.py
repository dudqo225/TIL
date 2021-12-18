import sys
sys.stdin = open('input.txt')

can_not = list(range(10, 21))

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())

    if A in can_not or B in can_not:
        ans = -1
    else:
        ans = A * B

    print('#{} {}'.format(tc, ans))