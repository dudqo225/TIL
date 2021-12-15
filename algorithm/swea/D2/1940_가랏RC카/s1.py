import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    command_list = []
    for _ in range(N):
        command = list(map(int, input().split()))
        command_list.append(command)

    ans = 0
    speed = 0

    while command_list:
        command = command_list.pop(0)
        if len(command) == 2:
            # command가 1일 때 가속
            if command[0] == 1:
                speed += command[1]
            # command가 2일 때 감속
            else:
                # 현재 속도보다 감속 속도가 클 경우, 속도는 0
                if speed < command[1]:
                    speed = 0
                # 아닐 경우, 현재 speed에서 command[1]만큼 감속
                else:
                    speed -= command[1]

        # 계산된 속도만큼 이동거리(ans) 증가
        ans += speed
    
    # 결과출력
    print('#{} {}'.format(tc, ans))