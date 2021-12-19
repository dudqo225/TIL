import sys
sys.stdin = open('input.txt')

A, B, V = map(int, input().split())

ans = 0
i = 0

while i < V:
    i += A
    if i >= V:
        i += B
    i -= B
    ans += 1

print(ans)