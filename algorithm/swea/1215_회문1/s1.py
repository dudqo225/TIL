import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):

    # palindrome 의 길이
    p = int(input())
    N= 8
    arr = [list(input()) for _ in range(N)]

    cnt = 0

    # 가로일 때

    for i in range(0, N):
        for j in range(0, N-p+1):
            if arr[i][j:j+p] == arr[i][j:j+p][::-1]:
                cnt += 1

    # 세로일 때
    for j in range(0, N):
        for i in range(0, N-p+1):
            char = ''
            for ci in range(i, i+p):
                char += arr[ci][j]
            if char == char[::-1]:
                cnt += 1

    # 결과 출력
    print('#{} {}'.format(tc, cnt))
