import sys
sys.stdin = open('input.txt')

number = int(input())
result = '홀수' if number % 2 else '짝수'
print(result)

numbers = list(map(int, input().split()))
total = 0

for number in numbers:
    total += number

print(total)


N = int(input())
matrix = []

for i in range(N):
    temp = list(map(int, input().split()))
    matrix.append(temp)

total_number = 0
for row in matrix:
    for number in row:
        total_number += number

print(total_number)