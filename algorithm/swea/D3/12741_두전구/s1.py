import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split(' '))

    lights = [0] * 101

    for i in range(A, B):
        lights[i] += 1

    for i in range(C, D):
        lights[i] += 1

    ans = 0
    for light in lights:
        if light == 2:
            ans += 1

    print('#{} {}'.format(tc, ans))