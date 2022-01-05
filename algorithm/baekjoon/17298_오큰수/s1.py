import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

for i in range(N-1):
    number = num[i]
    idx = N

    for j in range(i+1, N):
        if num[j] > number and j < idx:
            number = num[j]
            idx = j
    print(number if number != num[i] else -1, end=' ')
print(-1)