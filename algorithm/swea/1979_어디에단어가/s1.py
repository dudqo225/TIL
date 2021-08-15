import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for i in range(N):
        total = 0
        
        # 가로일 때
        for j in range(N):
            if arr[i][j] == 1:
                total += 1

            if arr[i][j] == 0 or j == N-1:
                if total == K:
                    cnt += 1
                total = 0
        
        # 세로일 때
        for j in range(N):
            if arr[j][i] == 1:
                total += 1

            if arr[j][i] == 0 or j == N-1:
                if total == K:
                    cnt += 1
                total = 0

    print('#{0} {1}'.format (tc, cnt))