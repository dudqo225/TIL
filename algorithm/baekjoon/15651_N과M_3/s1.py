import sys
sys.stdin = open('input.txt')

def DFS(a):
    if a == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):
        s.append(i)
        DFS(a+1)
        s.pop()

N, M = map(int, input().split())

s = []

DFS(0)