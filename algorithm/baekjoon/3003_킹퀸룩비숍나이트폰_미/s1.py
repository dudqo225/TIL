import sys
sys.stdin = open('input.txt')

chess = [1, 1, 2, 2, 2, 8]

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] != chess[i]:
        arr[i] = chess[i] - arr[i]
    else:
        arr[i] = 0

print(*arr)