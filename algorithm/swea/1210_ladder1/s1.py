import sys
sys.stdin = open('input.txt')

# 도착지에서 위로 올라가면서 출발지를 찾는 함수
def search(start):

    i = 99 # 행
    j = start # 열

    while i > 0: # 맨 윗줄에 도착하기 전까지 위로 올라감
        i -= 1 # 위로 한 칸 이동

        if j > 0 and ladder[i][j-1] == 1:         # 왼쪽 칸이 1이면
            while j > 0 and ladder[i][j-1] == 1:  # 사다리를 벗어나거나 0을 만날 때까지
                j -= 1                            # 왼쪽으로 이동

        elif j < 99 and ladder[i][j+1] == 1:      # 오른쪽 칸이 1이면
            while j < 99 and ladder[i][j+1] == 1: # 사다리를 벗어나거나 0을 만날 때까지
                j += 1                            # 오른쪽으로 이동

        # 좌우가 모두 0 이면 다시 위로 이동

    # 0번 행에 도착했을 때의 열(=출발지) 번호를 리턴
    return j

# 테스트 케이스 수는 10
T = 10
for tc in range(1, T+1):
    # n은 테스트 케이스 번호
    n = int(input())
    # 사다리 저장
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착지 검색
    # 도착지의 열 idx를 저장하는 goal 변수 초기화
    goal = 0
    # 사다리 100번 행의 i열의 값이 2이면 그 지점이 도착지이다.
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    
    # search 함수를 통해 결과값을 ans에 저장하고 출력
    ans = search(goal)
    print('#{} {}'.format(tc, ans))