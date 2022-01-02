import sys
sys.stdin = open('input.txt')

import math

N = int(input())

numbers = math.factorial(N)

numbers = str(numbers)[::-1]

ans = 0
for number in numbers:
    if number == '0':
        ans += 1
    else:
        print(ans)
        break