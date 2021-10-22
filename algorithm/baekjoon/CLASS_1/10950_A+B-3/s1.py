import sys

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())

    print(A + B)
