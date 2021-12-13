import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = int(input())

    ans = 0

    for i in range(num+1):
        if i % 2:
            ans += i
        else:
            ans -= i

    print('#{} {}'.format(tc, ans))