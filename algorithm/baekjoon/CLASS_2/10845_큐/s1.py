import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

queue = []

for _ in range(N):
    a = list(input().split())

    if a[0] == 'push':
        queue.append(a[1])
    elif a[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print('-1')
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')
    elif a[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print('-1')
    elif a[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print('-1')