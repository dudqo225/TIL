import sys
sys.stdin = open('input.txt')

def fibo(N):
    global zero, one

    if N == 0:
        zero += 1
        return 0
    elif N == 1:
        one += 1
        return 1
    else:
        return fibo(N-1) + fibo(N-2)

T = int(input())
for tc in range(1, T+1):
    number = int(input())

    zero, one = 0, 0

    fibo(number)

    print(zero, one)