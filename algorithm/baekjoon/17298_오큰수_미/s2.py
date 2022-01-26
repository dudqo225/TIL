import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

i = 0

while i < N-1:
    if num[i] > max(num[i+1:]):
        print(-1, end=' ')
    else:
        print(max(num[i+1:]), end=' ')

    i += 1
print(-1)