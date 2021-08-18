import sys
sys.stdin = open('input.txt')

# 테스트 케이스 T 입력
T = int(input())
# T만큼 반복
for tc in range(1, T+1):
    
    # 크기를 비교하기 위한 숫자 N, M 입력
    N, M = map(int, input().split())
    
    # 조건문. N이 M보다 클 경우 '>'
    if N > M:
        result = '>'
    # N과 M이 같을 경우 '='
    elif N == M:
        result = '='
    # N이 M보다 작을 경우 '<'
    else:
        result = '<'
    
    # 결과 출력
    print('#{} {}'.format(tc, result))