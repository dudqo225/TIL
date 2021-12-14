import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    ans = []
    for _ in range(N):
        alpha_num = list(input().split())
        for i in range(int(alpha_num[1])):
            ans.append(alpha_num[0])

    print('#{}'.format(tc))
    for i in range(0, len(ans), 10):
        print(*ans[i:i+10], sep='')