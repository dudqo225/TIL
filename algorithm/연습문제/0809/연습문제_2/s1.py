import sys
sys.stdin = open('input.txt')

N, M = list(map(int, input().split()))
matrix = []

for i in range(N):
    temp = list(map(int, input().split()))
    matrix.append(temp)

for i in range(N):
    total = 0
    for j in range(M):
        total += matrix[i][j]
    print(total)
