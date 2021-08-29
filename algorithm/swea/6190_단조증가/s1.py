import sys
sys.stdin = open('input.txt')

### 테스트 케이스 50개중에 49개 정답. 왜그런지 정말 모르겠다;;;

def findDan(lst):
    num_arr = set(lst)

    max_value = -1
    for num in num_arr:
        num_str = str(num)
        cnt = 0
        for i in range(len(num_str)-1):
            if num_str[i] <= num_str[i+1]:
                cnt += 1
        if cnt == len(num_str)-1 and num > max_value:
            max_value = num

    return max_value

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    num_multi = []
    for num in num_list:
        for i in range(N):
            if num >= num_list[i]:
                pass
            else:
                num_multi.append(num*num_list[i])

    dan = findDan(num_multi)

    print('#{} {}'.format(tc, dan))