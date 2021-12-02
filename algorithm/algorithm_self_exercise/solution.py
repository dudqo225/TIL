import sys
sys.stdin = open('eval_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = 5 # 지역 갯수
    location_name = ['서울', '대전', '구미', '부울경', '광주'] # 지역명

    M = int(input()) # 지역별 맛집 갯수

    location_mat = [list(map(int, input().split())) for _ in range(N)] # 지역별 맛집 레벨 리스트

    # 지역별 맛집 평균 구하기
    average_list = []
    for location in location_mat:
        total = 0
        for i in range(len(location)):
            total += location[i]
        average_list.append(round(total/M, 2))

    # 최대값 인덱스 찾기
    max_idx = max_val = 0
    for i in range(N):
        if average_list[i] > max_val:
            max_val = average_list[i]
            max_idx = i
    
    # 평균값 최대 지역명 변수 저장
    ans = location_name[max_idx]

    # 결과 출력
    print('#{} {}'.format(tc, ans))