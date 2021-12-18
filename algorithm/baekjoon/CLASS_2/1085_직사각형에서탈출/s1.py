import sys
sys.stdin = open('input.txt')

x, y, w, h = map(int, input().split())

ans = min(abs(x-w), abs(x-0), abs(y-h), abs(y-0))

print(ans)