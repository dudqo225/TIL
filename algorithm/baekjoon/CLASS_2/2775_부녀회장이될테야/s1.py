import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            people[j] += people[j-1]

    print(people[-1])