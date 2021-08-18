import sys
sys.stdin = open('input.txt')

# 테스트 케이스 T 개수 입력
T = int(input())

# T만큼 반복
for tc in range(1, T+1):
    # 10개의 수 입력
    num_list = list(map(int, input().split()))
    
    # 10개의 숫자의 총합 변수 초기화
    total = 0
    
    # 10개의 숫자를 반복하며 총합 변수에 더해준다.
    for i in num_list:
        total += i
    
    # 평균값을 구해서 result 변수에 할당. 평균값은 소수점 첫째 자리에서 반올림되어야 하므로 round() 함수 사용
    result = round(total / len(num_list))
    
    # 결과 출력
    print('#{} {}'.format(tc, result))

