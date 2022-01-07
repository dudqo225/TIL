import sys
sys.stdin = open('input.txt')

def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fibo(N-1) + fibo(N-2)

n = int(input())

ans = fibo(n)

print(ans)