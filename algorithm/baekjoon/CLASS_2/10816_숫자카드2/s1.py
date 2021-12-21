import sys
sys.stdin = open('input.txt')

N = int(input())

cards = list(map(int, input().split()))

M = int(input())

comparison_cards = list(map(int, input().split()))

ans = []

for card in comparison_cards:
    x = cards.count(card)
    ans.append(x)

print(*ans)