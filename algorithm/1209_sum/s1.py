import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    tc_num = int(input())
    
    # 100x100 array 배열 리스트 생성
    arr = [list(map(int, input().split())) for _ in range(100)]

    #행 합 구하기
    row_total_list = []
    for i in range(100):
        # 각 행의 합을 구하는 r_total 변수 초기화
        r_total = 0
        # 각 행의 합을 구하고, 그 값을 row_total_list 에 추가
        for j in range(100):
            r_total += arr[i][j]
        row_total_list.append(r_total)

    #열 합 구하기
    col_total_list = []
    for j in range(100):
        # 각 열의 합을 구하는 c_total 변수 초기화
        c_total = 0
        # 각 열의 합을 구하고, 그 값을 col_total_list 에 추가
        for i in range(100):
            c_total += arr[i][j]
        col_total_list.append(c_total)

    #좌>우 대각선 합 구하기
    l_diag_total = 0
    for i in range(100):
        l_diag_total += arr[i][i]

    #우>좌 대각선 합 구하기
    r_diag_total = 0
    # i는 0부터 +1씩, j는 N-1 부터 -1씩 감소하면서 순회
    for i in range(100):
        for j in range(99, -1, -1):
            # 대각의 합을 구해야 하기 때문에, 인덱스 값이 동일해야함
            if i + j == 99:
                r_diag_total += arr[i][i]


    #최대값 찾기
    find_max_value = [max(row_total_list), max(col_total_list), l_diag_total, r_diag_total]
    result = max(find_max_value)
    
    # 결과 출력
    print('#{0} {1}'.format (tc_num, result))

