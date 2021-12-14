import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    visited = [0] * 10

    i = 1
    while 0 in visited:
        num = i * N

        for j in str(num):
            idx = int(j)
            visited[idx] = 1

        i += 1

    print('#{} {}'.format(tc, num))