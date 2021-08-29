import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 T 입력
T = int(input())
for tc in range(1, T+1):
    # 농장 크기 N 입력
    N = int(input())
    
    # NxN 크기의 농장 입력
    arr = [list(map(int, input())) for _ in range(N)]
    
    # 중간값 구하기
    mid = N // 2
    
    # 반복문 인덱스의 시작점과 끝점 초기화
    start = mid
    end = mid
    
    # 수익 변수 초기화
    profit = 0
    
    # i는 0부터 N-1행까지 반복
    for i in range(N):
        # j는 행 인덱스가 mid와 같을 때까지 증가하고, 그 이후에는 다시 감소하는 규칙성을 보인다.
        for j in range(abs(start-i), abs(N-end)):
            # 수익 변수에 농작물 가치를 더해준다.
            profit += arr[i][j]
        # 반복문이 농장의 중간 행에 도달하기 전까지는 범위가 증가
        if i < mid:
            end -= 1
        # 중간 행 이후에는 범위가 다시 감소해야 한다.
        else:
            end += 1
    
    # 결과 출력
    print('#{} {}'.format(tc, profit))