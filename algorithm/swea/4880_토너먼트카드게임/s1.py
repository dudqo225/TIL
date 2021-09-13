import sys
sys.stdin = open('input.txt')

# 가위바위보 게임
def RPS(left, right):
    l, r = cards[left-1], cards[right-1]

    # 같을 경우, 인덱스가 낮은 사람이 이긴다.
    if l == r:
        return left
    # 가위
    elif l == 1:
        if r == 3:
            return left
        elif r == 2:
            return right
    # 바위
    elif l == 2:
        if r == 1:
            return left
        elif r == 3:
            return right
    # 보
    elif l == 3:
        if r == 1:
            return right
        elif r == 2:
            return left

# card game 함수
def cardGame(low, high):
    if low == high:
        return low
    else:
        # 중간 인덱스 설정
        mid = (low + high) // 2

        l = cardGame(low, mid)
        r = cardGame(mid+1, high)
        return RPS(l, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    cards = list(map(int, input().split()))

    ans = cardGame(1, N)

    print('#{} {}'.format(tc, ans))
