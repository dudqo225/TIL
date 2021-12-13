import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    tc_num = int(input())
    num_list = list(map(int, input().split()))
    num_cnt = [0] * 1001

    for num in num_list:
        num_cnt[num] += 1

    max_cnt = 0
    max_idx = 0
    for i in range(len(num_cnt)):
        if num_cnt[i] >= max_cnt:
            max_cnt = num_cnt[i]
            max_idx = i

    print('#{} {}'.format(tc_num, max_idx))