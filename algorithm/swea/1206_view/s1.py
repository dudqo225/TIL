import sys
sys.stdin = open('input.txt')

# 테스트 케이스는 총 10개
T = 10

# 10번의 테스트 케이스를 반복
for TC in range(1, T+1):
    # 건물 개수 (가로 길이) 저장
    TC_length = int(input())
    # 건물의 높이 리스트 저장
    buildingHeight = list(map(int, input().split()))
    
    # 조망권이 확보된 세대 수를 저장하는 result 변수 초기화
    result = 0
    
    # 맨 왼쪽 두 칸, 오른쪽 두 칸을 제외하고 건물을 반복
    for i in range(2, TC_length-2):
        # 해당 건물의 높이가 왼쪽으로 1, 2칸 건물과 오른쪽으로 1, 2칸 건물의 높이보다 높다면 조망권을 확보할 수 있음
        if buildingHeight[i] > buildingHeight[i-2] and buildingHeight[i] > buildingHeight[i-1] and buildingHeight[i] > buildingHeight[i+1] and buildingHeight[i] > buildingHeight[i+2]:

            #  비교하는 4개의 건물 중 가장 높은 값을 구하기 위해 변수를 초기화
            max_height = buildingHeight[i-2]
            # 왼쪽 2, 1칸 오른쪽 1, 2칸의 건물을 순회
            for j in range(-2, 3):
                # j가 0인 경우는 자기 자신이기 때문에 넘어간다.
                if j == 0:
                    continue
                # 4칸의 건물 중 가장 높은 건물의 높이를 구한다
                if buildingHeight[i-j] > max_height:
                    max_height = buildingHeight[i-j]
            # 기준이 되는 건물의 높이 - 비교 건물 중 가장 큰 건물의 높이 = 조망권 확보 세대. 이 값을 result 변수에 더해준다.
            result += buildingHeight[i] - max_height
    
    # 결과 값 출력
    print('#{0} {1}'.format (TC, result))