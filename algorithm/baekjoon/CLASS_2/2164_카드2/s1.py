import sys
sys.stdin = open('input.txt')

N = int(input())

cards = list(range(1, N+1))

while len(cards) > 1:
    cards.pop(0)
    temp = cards.pop(0)
    cards.append(temp)

print(cards[0])