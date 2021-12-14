import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    # A 회사
    A = P * W

    # B 회사
    if W > R:
        B = Q + (W-R) * S
    else:
        B = Q
    
    # 수도요금 비교
    if A > B:
        ans = B
    else:
        ans = A
    
    # 결과 출력
    print('#{} {}'.format(tc, ans))