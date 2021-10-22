import sys

sys.stdin = open('input.txt')

N = int(input())

arr = list(map(int, input().split()))

print('{} {}'.format(min(arr), max(arr)))