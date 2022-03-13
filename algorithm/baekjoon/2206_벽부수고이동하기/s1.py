import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
map = []

for _ in range(N):
    map.append(input())

print(map)