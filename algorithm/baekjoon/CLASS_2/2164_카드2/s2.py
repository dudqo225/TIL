import sys
sys.stdin = open('input.txt')

'''
s1.py 코드와의 차이점
일반 리스트 대신 collections의 deque를 사용
'''
from collections import deque

N = int(input())

cards = deque([i for i in range(1, N+1)])

while len(cards) > 1:
    cards.popleft()
    temp = cards.popleft()
    cards.append(temp)

print(cards[0])