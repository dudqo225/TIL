import sys
sys.stdin = open('input.txt')

K = int(input())

numbers = []

for _ in range(K):
    x = int(input())
    if x == 0:
        numbers.pop()
    else:
        numbers.append(x)

ans = sum(numbers)

print(ans)