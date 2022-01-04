import sys
sys.stdin = open('input.txt')

A, B, C = map(int, sys.stdin.readline().split())

if B > C:
    ans = -1
    print(ans)

i = 1

profit = C
cost = A + (B * 1)


while profit <= cost:
    i += 1
    profit = C * i
    cost = A + (B * i)

print(i)