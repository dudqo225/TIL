import sys
sys.stdin = open('input.txt')

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

N = int(input())

ans = factorial(N)
print(ans)
