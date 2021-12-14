import sys
sys.stdin = open('input.txt')

'''
SWEA 사이트에서는 C 언어로만 제출 가능
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    persons = list(map(int, input().split()))

    ans = 0

    visited = [0] * 100001
    min_distance = 100000
    for person in persons:
        if abs(person) <= min_distance:
            min_distance = abs(person)
            visited[abs(person)] += 1

    for dist, idx in enumerate(visited):
        if dist == min_distance:
            min_idx = idx

    print('#{} {} {}'.format(tc, min_distance, min_idx))