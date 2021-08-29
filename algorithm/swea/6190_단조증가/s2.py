import sys
sys.stdin = open('input.txt')

# 단조 증가하는 수 찾기
def findDan(number):
    num = str(number)

    # 규칙을 만족하는지 카운트 하는 변수 초기화
    cnt = 0
    for i in range(len(num)-1):
        # i번째 수가 i+1번째 수보다 크면 단조 증가하는 수가 아니므로 0을 리턴
        if num[i] > num[i+1]:
            return 0
        # 작거나 같으면 cnt + 1
        else:
            cnt += 1
    # cnt의 값이 숫자의 길이 -1과 동일하다면 단조 증가하는 수이므로 1을 리턴
    if cnt == len(num)-1:
        return 1

# 테스트 케이스 개수 T 입력
T = int(input())
for tc in range(1, T+1):
    # 테스트 케이스 정수 개수 N 입력
    N = int(input())
    # N개의 정수 리스트 입력
    num_list = list(map(int, input().split()))
    
    # 단조 증가하는 수 중 최대값 변수 초기화
    # 단조 증가하는 수가 하나도 없으면 -1을 출력하기 위해 -1로 초기화한다
    ans = -1
    
    # num_list의 숫자들을 반복 순회
    for i in range(N-1):
        for j in range(i+1, N):
            # temp 변수에 각 숫자의 곱을 할당
            temp = num_list[i] * num_list[j]
            # temp가 단조 증가하는 수이면서 최대값이면, 최대값을 변경
            if temp > ans and findDan(temp):
                ans = temp
    
    # 결과 출력
    print('#{} {}'.format(tc, ans))