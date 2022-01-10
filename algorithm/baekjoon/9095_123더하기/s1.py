import sys
sys.stdin = open('input.txt')

def dfs(start, ac_total):
    '''
    :param start: 시작숫자, 1로 Fix
    :param ac_total: 현재까지 누적합
    '''
    global ans
    if ac_total > n:
        return

    if ac_total == n:
        ans += 1
        return

    for i in range(1, 4):
        dfs(start, ac_total + i)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ans = 0
    dfs(1, 0)
    print(ans)