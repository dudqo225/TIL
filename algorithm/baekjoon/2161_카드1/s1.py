import sys
sys.stdin = open('input.txt')

N = int(input())

cards = list(range(1, N+1))

while len(cards) > 1:
    junk_card = cards.pop(0)
    print(junk_card, end=' ')
    move_card = cards.pop(0)
    cards.append(move_card)

print(cards[0])