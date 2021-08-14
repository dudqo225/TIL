import sys
sys.stdin = open('input.txt')

# 테스트 횟수 T
T = int(input())

# T번 테스트 케이스를 반복
for TC in range(1, T+1):
    # NxN 2차 배열의 N값 불러오기
    N = int(input())

    # arr에 NxN 배열 리스트 저장
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타 리스트 생성 i는 행, j는 열. 방향은 우하좌상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 절대값 총합을 구하기 위한 total 변수 초기화
    total = 0

    # i를 N번 반복 (행)
    for i in range(N):
        # j를 N번 반복 (열)
        for j in range(N):
            # k 를 4번 반복 (우하좌상)
            for k in range(4):
                # 현 위치 요소에 델타 값을 더한 값을 이웃한 요소의 인덱스 ni와 nj에 저장
                ni = i + di[k]
                nj = j + dj[k]
                # ni와 nj가 NxN 범위를 벗어나지 않을 경우
                if 0 <= ni < N and 0 <= nj < N:
                    # 각 요소와 이웃한 요소들의 차이의 절대값을 total에 더해준다.
                    total += abs(arr[i][j] - arr[ni][nj])
    
    # 결과값 출력
    print('#{0} {1}'.format(TC, total))