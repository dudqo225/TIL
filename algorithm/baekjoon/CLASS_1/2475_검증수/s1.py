import sys

sys.stdin = open('input.txt')

arr = map(int, input().split())

total = 0

for num in arr:
    total += num**2

ans = total % 10

print(ans)