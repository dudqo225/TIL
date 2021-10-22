import sys

sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input()))

print(sum(arr))
