import sys
sys.stdin = open('input.txt')

'''
문제
숙소에 긴 복도를 따라 총 400개의 방이 배열되어 있다.
수련회에 간 학생들이 밤 12시가 되어 조교들의 눈을 피해 각자 자기방으로 돌아가려 한다.
지나는 복도의 구간이 겹치면 두 학생은 동시에 돌아갈 수 없다.
최소 몇 단위시간만에 모든 학생들이 이동할 수 있는지 구하시오.

입력
입력은 T개의 테스트 케이스로 되어 있다. 각 테스트 케이스 첫 줄에는 돌아가야 할 학생들의 수 N이 주어진다.
다음 N 줄에는 각 학생의 현재 방 번호와 돌아가야 할 방의 번호가 주어진다.

출력
테스트 케이스 T에 대한 결과는 '#T'을 찍고, 각 테스트 케이스마다 필요한 시간을 한 줄에 하나씩 출력한다.
'''

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