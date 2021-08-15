import sys
sys.stdin = open('input.txt')

# 도착지에서 위로 올라가는 함수
def search(start):

    i = 99 # 행
    j = start # 열

    while i > 0: # 맨 윗줄에 도착하기 전까지 위로 올라감
        i -= 1 # 위로 한 칸 이동

        if j > 0 and ladder[i][j-1] == 1:         # 왼쪽 칸이 1이면
            while j > 0 and ladder[i][j-1] == 1:  # 사다리를 벗어나거나 0을 만날 때까지
                j -= 1                            # 왼쪽으로 이동

        elif j < 99 and ladder[i][j+1] == 1:      # 오른쪽 칸이 1이면
            while j < 99 and ladder[i][j+1] == 1:
                j += 1

        # 좌우가 0이면 위로

    return j # 0번 행에 도착했을 때의 열(출발지)를 리턴


T = 10
for tc in range(1, T+1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착지 검색
    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i

    ans = search(goal)
    print('#{} {}'.format(tc, ans))