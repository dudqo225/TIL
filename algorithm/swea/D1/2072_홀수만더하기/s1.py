import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 T 입력
T = int(input())
# T만큼 반복
for tc in range(1, T+1):
    # 숫자들의 리스트 입력
    num_list = list(map(int, input().split()))
    
    # 총합 변수 total 초기화
    total = 0
    
    # 숫자 리스트를 순회하며, i 가 홀수일 때 total에 더해준다.
    for i in num_list:
        if i % 2:
            total += i
    
    # 결과 출력
    print('#{} {}'.format(tc, total))