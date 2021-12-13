import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = input()

    if words == words[::-1]:
        ans = 1
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))