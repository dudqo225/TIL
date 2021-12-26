import sys
sys.stdin = open('input.txt')

N = int(input())

check = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())

    check[num] += 1

for i in range(10001):
    if check[i] != 0:
        for j in range(check[i]):
            print(i)