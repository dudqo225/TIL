import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 T 입력
T = int(input())

# 1~12월별 유효 날짜 리스트 생성 
md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# T만큼 반복
for tc in range(1, T+1):
    
    # 8자리 날짜 입력
    date_str = input()
    # 연도 슬라이싱
    year = (date_str[0:4])
    # 월 슬라이싱
    month = (date_str[4:6])
    # 일 슬라이싱
    day = (date_str[6:])
    # 유효하지 않은 날짜일 경우 -1 값을 출력하기 위해 res 변수 생성
    res = -1
    
    # month의 값이 1~12 사이에 없을 경우  
    if int(month) < 1 or int(month) > 12:
        print('#{} {}'.format(tc, res))
    
    # month 값이 유효할 경우
    else:
        # month가 1, 3, 5, 7, 8, 10, 12월일 경우
        if int(month) == 1 and int(month) == 3 and int(month) == 5 and int(month) == 7 and int(month) == 8 and int(month) == 10 and int(month) == 12:
            # 해당 월의 날짜가 유효하지 않을 경우
            if int(day) < 1 or int(day) > 31:
                print('#{} {}'.format(tc, res))
            # 월의 날짜가 유효할 경우
            else:
                print('#{} {}/{}/{}'.format(tc, year, month, day))
        # month가 2월일 경우
        elif int(month) == 2:
            # 해당 월의 날짜가 유효하지 않을 경우
            if int(day) < 1 or int(day) > 28:
                print('#{} {}'.format(tc, res))
            # 월의 날짜가 유효할 경우
            else:
                print('#{} {}/{}/{}'.format(tc, year, month, day))
        # 위 경우를 제외한 나머지 month의 경우        
        else:
            # 해당 월의 날짜가 유효하지 않을 경우
            if int(day) < 1 or int(day) > 30:
                print('#{} {}'.format(tc, res))
            # 월의 날짜가 유효할 경우
            else:
                print('#{} {}/{}/{}'.format(tc, year, month, day))