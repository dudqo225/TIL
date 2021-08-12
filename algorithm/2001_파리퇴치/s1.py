import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 T 입력
T = int(input())

# 테스트 케이스 수만큼 반복
for tc in range(1, T+1):

    # N, M 값 입력
    N, M = map(int, input().split())

    # NxN 으로 이루어진 배열 arr 입력
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대로 죽은 파리 수를 저장하는 result 리스트 생성
    result = []

    # NxN 행렬을 순회
    for i in range(N-1):
        for j in range(N-1):
            # i행 j열에서 죽인 파리 수를 저장하는 total 변수 초기화
            total = 0
            # i, j 기준 MxM 파리채를 내리쳐 파리를 잡는다.
            for x in range(0, M):
                for y in range(0, M):
                    # 인덱스 범위 안에 있다면 total에 각 영역의 파리수를 저장
                    if 0 <= i+x < N and 0 <= j+y < N:
                        total += arr[i+x][j+y]
            # result 리스트에 total 값을 각각 추가
            result.append(total)
    
    # 최대값 찾기
    max_value = result[0]
    for num in result:
        if num > max_value:
            max_value = num
    
    # 결과 출력
    print('#{0} {1}'.format (tc, max_value))