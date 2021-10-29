import sys
sys.stdin = open('input.txt')

C = int(input())

for tc in range(1, C+1):
    arr = list(map(int, input().split()))

    N = arr[0]
    scores = arr[1:]

    over_cnt = 0
    avg = sum(scores)/N

    for score in scores:
        if score > avg:
            over_cnt += 1

    ans = over_cnt / N * 100

    print('{:.3f}%'.format(ans))
