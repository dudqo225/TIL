import sys
sys.stdin = open('input.txt')

def binarySearch(page, target):

    left = 1
    right = page
    cnt = 0

    while left <= right:
        middle = int((left + right) / 2)

        if middle == target:
            return cnt
        elif middle > target:
            right = middle
            cnt += 1
        else:
            left = middle
            cnt += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    Pa_cnt = binarySearch(P, Pa)
    Pb_cnt = binarySearch(P, Pb)

    if Pa_cnt > Pb_cnt:
        result = 'B'
    elif Pa_cnt < Pb_cnt:
        result = 'A'
    else:
        result = 0

    print('#{} {}'.format(tc, result))


