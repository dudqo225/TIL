import sys
sys.stdin = open('input.txt')

# 영역을 계산하는 paper 함수 생성
def paper(n):
    
    # n이 1일 경우, 1을 반환
    if n == 1:
        return 1
    # n이 2일 경우, 3을 반환
    elif n == 2:
        return 3
    # 그외의 경우. 점화식으로 표현
    else:
        return paper(n-1) + paper(n-2) * 2

# 테스트 케이스 개수 T 입력
T = int(input())

# T만큼 반복
for tc in range(1, T+1):
    # N 값 입력
    N = int(input())
    
    # N을 10으로 나눈 수를 n에 저장
    n = N // 10
    
    # 결과 출력
    print('#{} {}'.format(tc, paper(n)))