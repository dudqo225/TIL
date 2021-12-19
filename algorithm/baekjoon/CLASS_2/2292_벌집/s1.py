import sys
sys.stdin = open('input.txt')

N = int(input())

num, ans, i = 1, 1, 1

while num < N:
    num += i * 6
    ans += 1
    i += 1

print(ans)