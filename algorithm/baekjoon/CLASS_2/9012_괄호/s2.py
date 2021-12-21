import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    ps = list(input())

    i = 0

    for p in ps:
        if p == '(':
            i += 1
        else:
            i -= 1

        if i < 0:
            print('NO')
            break

    if i > 0:
        print('NO')
    elif i == 0:
        print('YES')