import sys
sys.stdin = open('input.txt')

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

M, N = map(int, input().split())

numbers = list(range(M, N+1))

for number in numbers:
    res = is_prime_number(number)
    if res == True:
        print(number)