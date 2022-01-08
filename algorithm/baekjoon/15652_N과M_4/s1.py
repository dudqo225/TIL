import sys
sys.stdin = open('input.txt')

def DFS(start, depth):
    if depth == M:
        print(' '.join(map(str, s)))
        return

    for i in range(start, N+1):
        s.append(i)
        DFS(i, depth+1)
        s.pop()

N, M = map(int, input().split())

s = []

DFS(1, 0)