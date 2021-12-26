import sys
sys.stdin = open('input.txt')

N = int(input())

numbers = []

for _ in range(N):
    number = int(input())
    numbers.append(number)

numbers = sorted(numbers)

for number in numbers:
    print(number)