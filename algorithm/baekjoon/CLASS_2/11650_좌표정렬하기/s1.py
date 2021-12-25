import sys
sys.stdin = open('input.txt')

N = int(input())

coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append([x, y])

coordinates = sorted(coordinates, key= lambda x: (x[0], x[1]))

for coordinate in coordinates:
    print('{} {}'.format(coordinate[0], coordinate[1]))