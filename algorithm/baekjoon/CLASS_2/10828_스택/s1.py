import sys

sys.stdin = open('input.txt')

# 백준에서 시간초과가 날 때 'input = sys.stdin.readline' 을 사용하면 해결된다.
input = sys.stdin.readline


N = int(input())

stack = []
for _ in range(N):
    a = list(input().split())
    if 'push' in a:
        stack.append(a[1])
    elif 'pop' in a:
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif 'size' in a:
        print(len(stack))
    elif 'empty' in a:
        if stack:
            print('0')
        else:
            print('1')
    else:
        if stack:
            print(stack[-1])
        else:
            print('-1')