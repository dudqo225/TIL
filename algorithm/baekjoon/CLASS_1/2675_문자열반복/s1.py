import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    R, S = input().split()

    for i in S:
        print(i*int(R), end='')
    print()