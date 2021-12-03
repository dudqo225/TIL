import sys
sys.stdin = open('input.txt')

'''
파이썬 내장 itertools의 순열(Permutations)을 활용
중간 과정에서 가지치기가 없어서 런타임 에러가 발생한다.
N이 최대 16일때 16! 을 계산해야 하다보니, 런타임 에러가 발생하는 듯 하다.
'''


import itertools

def cal_percentage(lst):
    global mat

    per_val = 1
    for i in range(N):
        per_val *= mat[i][lst[i]]*0.01

    return per_val

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    arr = list(range(N))
    permu_list = list(itertools.permutations(arr, N))

    max_per = 0
    for permu in permu_list:
        val = cal_percentage(permu)
        if val > max_per:
            max_per = val

    ans = format(max_per*100, ".6f")
    print('#{} {}'.format(tc, ans))