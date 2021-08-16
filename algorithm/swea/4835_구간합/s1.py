import sys
sys.stdin = open('input.txt')

# 테스트 케이스 T 불러오기
T = int(input())

# 테스트 케이스 반복
for TC in range(1, T+1):
    # 정수 개수 N과 구간 개수 M 불러오기
    N, M = map(int, input().split())
    # N개의 정수값 불러오기
    numbers = list(map(int, input().split()))

    # 구간별 합 저장을 위한 빈 리스트 생성
    result = []
    # N-M+1번 반복하기
    for i in range(0, N-M+1):
        # 임시 저장값 temp 초기화
        temp = 0
        # 구간만큼 반복하며 이웃한 M개의 합을 계산
        for j in range(0, M):
            temp += numbers[i+j]
        # result 리스트에 추가
        result.append(temp)

    # 구간합이 가장 크고 작은 value 구하기
    max_value = result[0]
    min_value = result[0]
    for num in result:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num

    # 결과 출력
    print('#{} {}'.format(TC, max_value-min_value))


