import sys
sys.stdin = open('input.txt')

# 테스트는 총 10개
T = 10

# 10개의 테스트 케이스를 반복
for TC in range(1, T+1):
    # 덤프 횟수 받아오기
    dump = int(input())
    # 각 상자의 높이값 받아서 리스트로 저장
    box_list = list(map(int, input().split()))

    # 덤프 횟수가 0이 될 때까지 반복
    while dump > 0:
        
        # 최대값과 인덱스, 최소값과 인덱스를 초기화
        max_value = box_list[0]
        max_idx = 0
        min_value = box_list[0]
        min_idx = 0

        # box_list 를 순회하며, 최대값과 인덱스, 최소값과 인덱스를 찾는다.
        for idx, value in enumerate(box_list):
            if value > max_value:
                max_value = value
                max_idx = idx
            elif value < min_value:
                min_value = value
                min_idx = idx

        # box_list의 최대값에서 1을 빼고, 최소값에 1을 더해준다.
        box_list[max_idx] -= 1
        box_list[min_idx] += 1

        # 한 번의 덤프가 끝났기 때문에, dump 값에 -1 해준다.
        dump -= 1

    # 주어진 덤프가 완료된 후, 최대값과 최소값을 찾기 위해 변수를 초기화한다.
    max_value = box_list[0]
    min_value = box_list[0]

    # box_list 를 순회하며 최대값과 최소값을 찾는다.
    for box in box_list:
        if box > max_value:
            max_value = box
        elif box < min_value:
            min_value = box

    # 덤프 횟수가 줄어들기 전에 평탄화가 끝날 경우
    if max_value - min_value == 0 or max_value - min_value == 1:
        print(max_value - min_value)
    
    # 결과값 출력
    print('#{0} {1}'.format (TC, max_value - min_value))
