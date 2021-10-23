import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
N = int(input())

deque = []

for _ in range(N):
    a = list(input().split())

    if a[0] == 'push_front':
        deque.insert(0, a[1])
    elif a[0] == 'push_back':
        deque.append(a[1])
    elif a[0] == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print('-1')
    elif a[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print('-1')
    elif a[0] == 'size':
        print(len(deque))
    elif a[0] == 'empty':
        if deque:
            print('0')
        else:
            print('1')
    elif a[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print('-1')
    elif a[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print('-1')