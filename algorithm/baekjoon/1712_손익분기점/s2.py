import sys
sys.stdin = open('input.txt')

A, B, C = map(int, sys.stdin.readline().split())

if B >= C:
    ans = -1
else:
    ans = (A // (C-B)) + 1

print(ans)