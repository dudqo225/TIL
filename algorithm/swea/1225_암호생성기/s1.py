import sys
sys.stdin = open('input.txt')

# 테스트 케이스는 총 10개
T = 10
# 10번 테스트를 반복
for tc in range(1, T+1):
    # 테스트 케이스 번호 입력
    tc_num = int(input())

    # 8개의 숫자를 리스트 형태로 입력
    num_list = list(map(int, input().split()))

    # 리스트의 마지막 값이 0이 될 때까지 반복
    while num_list[-1] != 0:
        # 한 사이클은 1~5씩 감소한다.
        for i in range(1, 6):
            # 리스트의 첫번째 원소를 pop하고 i만큼 뺀 값을 임시 변수 temp에 저장
            temp = num_list.pop(0) - i
            # temp의 값이 0보다 작거나 같으면 값을 0으로 고정하고 리스트 마지막에 추가한 후 프로그램을 종료
            if temp <= 0:
                temp = 0
                num_list.append(temp)
                break
            # 그렇지 않으면 리스트의 마지막에 추가
            num_list.append(temp)
    
    # 결과 출력. 테스트 케이스 번호를 먼저 출력
    print('#{}'.format(tc_num), end=' ')
    # num_list를 순회하면서 8자리 암호를 출력한다.
    for num in num_list:
        print(num, end=' ')
    print()