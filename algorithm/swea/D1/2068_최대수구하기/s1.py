import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 T 입력
T = int(input())
# T만큼 반복
for tc in range(1, T+1):
    # 숫자 리스트 입력
    num_list = list(map(int, input().split()))
    
    # 최대값을 숫자 리스트의 0번째 수로 초기화
    max_num = num_list[0]
    
    # 리스트를 순회하며 i가 현재 최대값보다 크면, 최대값을 i로 변경
    for i in num_list:
        if i > max_num:
            max_num = i
    
    # 결과 출력
    print('#{} {}'.format(tc, max_num))