import sys
sys.stdin = open('input.txt')

# 테스트 케이스 T 입력
T = int(input())

# T만큼 테스트 반복
for tc in range(1, T + 1):
    # 배열의 행열 수 N과 파리채의 크기 M 입력
    N, M = map(int, input().split())

    # NxN 배열 입력
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 영역별로 죽은 파리 수를 저장하는 빈 리스트 생성
    fly = []

    # i는 0부터 N-1까지
    for i in range(N-M+1):
        # j는 0부터 N-1까지
        for j in range(N-M+1):
            # 영역별 파리수 총합을 저장하는 변수 초기화
            total = 0
            # ci는 0부터 M-1까지
            for ci in range(M):
                # cj는 0부터 M-1까지
                for cj in range(M):
                    # 인덱스의 범위안에 해당하면, total 변수에 파리수를 저장
                    if i + ci in range(N) and j + cj in range(N):
                        total += mat[i + ci][j + cj]
            # 영역별 파리수 총합을 fly 리스트에 추가            
            fly.append(total)
    
    # 최대값을 fly 0번째 인덱스의 값으로 초기화
    max_value = fly[0]
    # fly 리스트를 순회
    for i in fly:
        # i의 값이 최대값보다 크면, i값을 최대값으로 변경
        if i > max_value:
            max_value = i
    
    # 결과 출력
    print('#{} {}'.format(tc, max_value))