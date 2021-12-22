import sys
sys.stdin = open('input.txt')

# 세로, 가로
N, M = map(int, input().split())

chess = [[i for i in input()] for _ in range(N)]

results = []

for i in range(N-7):
    for j in range(M-7):
        w_cnt = 0
        b_cnt = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if chess[x][y] != 'W':
                        w_cnt += 1
                    if chess[x][y] != 'B':
                        b_cnt += 1
                else:
                    if chess[x][y] != 'B':
                        w_cnt += 1
                    if chess[x][y] != 'W':
                        b_cnt += 1
        results.append(min(w_cnt, b_cnt))

ans = min(results)

print(ans)