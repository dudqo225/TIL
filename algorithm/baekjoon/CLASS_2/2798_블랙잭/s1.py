import sys
from itertools import combinations

sys.stdin = open('input.txt')

N, M = map(int, input().split())

num_list = list(map(int, input().split()))

com_list = list(combinations(num_list, 3))

biggest_total = 0

for com in com_list:
    temp_total = sum(com)

    if biggest_total < temp_total <= M:
        biggest_total = temp_total

print(biggest_total)

'''
파이썬 내장함수 itertools의 combinations(조합)을 사용하여 풀이하였다.
combinations(조합을 찾고자 하는 순회가능한 리스트/튜플, 조합할 수) 로 코드를 작성하고 이를 list()로 감싸면
리스트 내부에 튜플 형태로 조합이 저장된다.
'''