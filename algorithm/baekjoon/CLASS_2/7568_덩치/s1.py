import sys
sys.stdin = open('input.txt')

N = int(input())

persons = []

for _ in range(N):
    w, h = map(int, input().split())
    persons.append([w, h])

for person in persons:
    rank = 1
    for people in persons:
        if  person[0] < people[0] and person[1] < people[1]:
            rank += 1
    print(rank, end=' ')