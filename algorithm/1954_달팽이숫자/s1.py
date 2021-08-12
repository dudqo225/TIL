import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    # 델타 리스트 생성. 우 - 하 - 좌 - 상
    di = [0, 1, 0, -1] 
    dj = [1, 0, -1, 0] 

    # 현재 방향 0=우, 1=하, 2=좌, 3=상
    k = 0

    # arr 0,0 에 첫번째 달팽이 숫자 입력
    n = 1
    i, j = 0, -1

    #
    while n <= N * N:
        ci = i + di[k]
        cj = j + dj[k]

        if 0 <= ci < N and 0 <= cj < N and arr[ci][cj] == 0:
            arr[ci][cj] = n
            n += 1
            i, j = ci, cj

        else:
            k = (k + 1) % 4

    print('#{}'.format (TC))
    for row in arr:
        for num in row:
            print(num, end=' ')
        print()
