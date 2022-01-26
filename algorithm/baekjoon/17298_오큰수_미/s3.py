import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

ans = [-1] * N

stack = [0]

for i in range(1, N):
    while stack and num[stack[-1]] < num[i]:
        ans[stack.pop(0)] = num[i]


