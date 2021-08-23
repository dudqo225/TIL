import sys
sys.stdin = open('input.txt')

P, K = map(int, input().split())

cnt = 0

while P >= K:
    cnt += 1
    K += 1

print(cnt)