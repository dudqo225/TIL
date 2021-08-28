import sys
sys.stdin = open('input.txt')

# 테스트 케이스 수
T = int(input())

# T만큼 반복
for tc in range(1, T+1):

    # 돌아가야 할 학생 수 N 입력
    N = int(input())
    
    # 복도 리스트 생성
    corridor = [0] * 200
    
    # N만큼 반복하며
    for _ in range(N):
        # 현재방 s, 돌아갈 방 e를 입력
        s, e = map(int, input().split())
        
        # s가 e보다 작거나 같으면
        if s <= e:
            # 반복을 s -> e 로 순회하며 복도 리스트의 i번째 인덱스에 1씩 더해준다.
            for i in range((s-1)//2, (e-1)//2+1):
                corridor[i] += 1
        # s가 e보다 클 경우                
        else:
            # 반복을 e -> s 로 순회하며 복도 리스트의 i번째 인덱스에 1씩 더해준다.
            for i in range((e-1)//2, (s-1)//2+1):
                corridor[i] += 1
    
    # 복도의 0번째 값을 최대값으로 초기화
    max_value = corridor[0]
    # 복도 리스트를 순회하면서 최대값을 찾아준다. (최대값 = 모든 학생들이 방으로 돌아가는 최소 단위시간)
    for corr in corridor:
        if corr > max_value:
            max_value = corr
    
    # 결과 출력
    print('#{} {}'.format(tc, max_value))