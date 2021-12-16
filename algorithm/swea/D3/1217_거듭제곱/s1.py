import sys
sys.stdin = open('input.txt')

'''
일반적인 for 문을 활용하여 문제를 해결한 코드
'''

T = 10
for tc in range(1, T+1):
    tc_num = int(input())
    N, M = map(int, input().split())

    ans = 1

    for _ in range(M):
        ans *= N

    print(ans)