import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    
    # 최대, 최소값 찾기
    max_val, min_val = 0, 10001
    for num in num_list:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    # 최대, 최소값 제외한 나머지의 합을 저장하는 변수
    avg_num_total = 0
    for num in num_list:
        if num == max_val or num == min_val:
            pass
        else:
            # 나머지의 합 계산
            avg_num_total += num
    
    # 나머지의 평균값 계산 - round() 메서드를 이용해서 소수점 첫째자리에서 반올림하기
    ans = round(avg_num_total / 8)
    # ans = avg_num_total // 8 - 테케 4개가 오답처리됨.
    
    # 결과 출력
    print('#{} {}'.format(tc, ans))