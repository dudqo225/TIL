import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 T 입력
T = int(input())

# T번의 테스트 반복
for tc in range(1, T+1):
    
    # 원소 개수 N, 원소의 합 K 값 입력
    N, K = map(int, input().split())

    # 1부터 12까지 숫자로 이루어진 arr 리스트 생성, n은 arr 리스트의 길이
    arr = list(range(1, 13))
    n = len(arr)

    # N개의 원소를 갖고 있는 부분 집합의 리스트를 저장하는 변수 생성
    total_list=[]

    # 부분 집합 전체를 찾는 과정을 반복
    for i in range(1<<n):
        # 부분 집합을 저장하는 변수 생성
        sub_list = []
        # 비트 연산을 통해 조건이 일치하면 sub_list에 부분 집합을 추가
        for j in range(n):
            if i & (1<<j):
                sub_list.append(arr[j])
        # 부분집합의 길이가 N이면 total_list에 추가
        if len(sub_list) == N:
            total_list.append(sub_list)
    
    # 원소의 합이 K인 부분집합의 수를 세는 cnt 변수 생성
    cnt = 0
    
    # total_list를 순회
    for sub in total_list:
        # 원소의 합 변수 초기화
        total = 0
        # 부분집합을 순회하며 원소들의 합을 계산
        for num in sub:
            total += num
        # 부분집합 내 원소들의 합이 K이면, cnt에 1을 더해준다
        if total == K:
            cnt += 1
    
    # 결과 출력
    print('#{0} {1}'.format (tc, cnt))

