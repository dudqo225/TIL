import sys
sys.stdin = open('input.txt')

N = int(input())

cnt = 0

while N > 1:
    print(N)
    if N % 3 == 0:
        N /= 3
        cnt += 1
    elif N % 2 == 0:
        N /= 2
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)