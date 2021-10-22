import sys
sys.stdin = open('input.txt')

A = int(input())
B = int(input())
C = int(input())

arr = A * B * C

result = [0] * 10

for i in str(arr):
    result[int(i)] += 1

for res in result:
    print(res)