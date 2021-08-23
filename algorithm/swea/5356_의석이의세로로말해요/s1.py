import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    result = ''
    max_len = 0
    for i in range(5):
        if len(arr[i]) > max_len:
            max_len = len(arr[i])

    for i in range(max_len):
        for j in range(5):
            if i < len(arr[j]):
                result += arr[j][i]

    print('#{} {}'.format(tc, result))