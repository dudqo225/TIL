# sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pocketmon_book = [0]

for _ in range(N):
    pocketmon = input().rstrip()
    pocketmon_book.append(pocketmon)

for i in range(M):
    val = input().rstrip()
    if val.isalpha():
        print(pocketmon_book.index(val))
    else:
        print(pocketmon_book[int(val)])