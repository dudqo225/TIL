import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 T 입력
T = int(input())
for tc in range(1, T+1):
    # 숫자 N, M 입력
    N, M = map(int, input().split())
    
    # N개로 이루어진 숫자열 A와 M개로 이루어진 숫자열 B 입력
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # 최대값 초기화
    max_value = 0
    
    # 숫자열 B의 길이가 A보다 길 경우
    if N < M:
        for i in range(M-N+1):
            total = 0
            for j in range(i, i+N):
                total += A[j-i] * B[j]
            if total > max_value:
                max_value = total
    
    # 숫자열 A의 길이가 B보다 길 경우
    elif N > M:
        for i in range(N-M+1):
            total = 0
            for j in range(i, i+M):
                total += B[j-i] * A[j]
            if total > max_value:
                max_value = total
    
    # 결과 출력
    print('#{} {}'.format(tc, max_value))