import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    # 가로일때
    for i in range(0, N):
        for j in range(0, N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                result = arr[i][j:j+M]

    # 세로일때
    for j in range(0, N):
        char = ''
        for i in range(0, N-M+1):
            for ci in range(i, i+M):
                char += arr[ci][j]
        if char == char[::-1]:
            result = char

    print('#{} '.format(tc))
    for char in result:
        print(char, end='')
    print()

