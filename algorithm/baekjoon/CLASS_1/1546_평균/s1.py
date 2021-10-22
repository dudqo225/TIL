import sys

sys.stdin = open('input.txt')

N = int(input())

scores = list(map(int, input().split()))

max_score = max(scores)

total = 0
for score in scores:
    total += score/max_score*100

print(total/N)