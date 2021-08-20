import sys
sys.stdin = open('input.txt')

# 테스트 케이스 T 입력
T = int(input())

# T만큼 반복
for tc in range(1, T+1):
    # 버스 노선 N개 입력
    N = int(input())

    # 각 노선별로 어떤 정류장을 지나는지 체크하기 위해 stop 변수 생성
    # 5001개를 만드는 이유는 0번 인덱스부터 5000번 인덱스까지로 표현하기 위함. (0번 인덱스는 의미X)
    stop = [0] * 5001

    # N만큼 반복
    for i in range(N):
        # Ai와 Bi 에 출발/도착 정류장 값을 입력
        Ai, Bi = map(int, input().split())
        # Ai부터 Bi까지 반복하며
        for j in range(Ai, Bi +1):
            # 정류장의 j번째 인덱스에 1씩 더해준다. (해당 정류장을 통과한다는 의미)
            stop[j] += 1

    # P개의 버스 정류장 입력
    P = int(input())

    # P개의 버스 정류장을 저장하는 c_list 생성
    c_list = []

    # P만큼 반복
    for i in range(P):
        # 버스정류장 번호를 temp 변수에 저장하고, c_list에 추가
        temp = int(input())
        c_list.append(temp)

    # 결과 출력
    print('#{}'.format(tc), end=' ')
    for i in c_list:
        print(stop[i], end=' ')
    print()