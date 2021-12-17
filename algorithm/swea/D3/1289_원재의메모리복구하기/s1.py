import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    bits = input()

    origin = []

    for bit in bits:
        origin.append(int(bit))

    initial = [0] * len(origin)

    cnt = 0
    i = 0
    while origin != initial:
        if origin[i] != initial[i]:
            for j in range(i, len(origin)):
                if initial[j] == 0:
                    initial[j] = 1
                else:
                    initial[j] = 0
            cnt += 1
            i = 0
        else:
            i += 1

    print('#{} {}'.format(tc, cnt))