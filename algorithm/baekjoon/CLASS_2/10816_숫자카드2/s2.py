import sys
sys.stdin = open('input.txt')

'''
일반적인 파이썬 내장 .count()를 사용하면, 시간초과 문제를 해결할 수 없다.
따라서 collections의 Counter 함수를 사용하여 시간복잡도 문제를 해결한다.
'''

from collections import Counter

N = int(input())

cards = list(map(int, input().split()))

M = int(input())

comparison_cards = list(map(int, input().split()))

cnt = Counter(cards)

for card in comparison_cards:
    if card in cnt:
        print(cnt[card], end=' ')
    else:
        print('0', end=' ')