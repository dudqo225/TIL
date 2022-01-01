import sys
sys.stdin = open('input.txt')

def fibo(N):
    global zero, one

    if N > 2:
        for i in range(3, N+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

T = int(input())
for tc in range(1, T+1):
    number = int(input())

    zero = [1, 0, 1]
    one = [0, 1, 1]

    fibo(number)

    print(zero[number], one[number])