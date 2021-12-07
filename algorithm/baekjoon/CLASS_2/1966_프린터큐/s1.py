import sys
sys.stdin = open('input.txt')

'''
Q 값과 인덱스를 저장하는 리스트를 각각 생성한다 -> Q / Q_idx
조건에 따라 Q의 0번째 인덱스 값이 최대값이 나올 때까지 Q를 pop / append로 조작한다.
Q의 0번째 인덱스 문서가 최대값일 경우, Q에서 제거하고 cnt를 1증가.
목표 문서 및 인덱스와 일치하면 while 반복문을 종료한다.
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split())) # 인쇄할 문서 저장
    Q_idx = list(range(N))              # 인쇄할 문서의 순서 저장

    cnt = 0
    obj = Q[M]
    obj_idx = Q_idx[M]
    while Q:
        if Q[0] == max(Q):
            cnt += 1 # Q의 첫번째 값이 최대값이면 문서를 인쇄하고 cnt를 1 증가.
            if Q[0] == obj and Q_idx[0] == obj_idx: # Q의 첫번째 값이 목표 문서, 인덱스와 일치하면 while문 break
                break

        temp = Q.pop(0)
        temp_idx = Q_idx.pop(0)

        for i in range(len(Q)):
            if temp < Q[i]:
                Q.append(temp)
                Q_idx.append(temp_idx)
                break

    print(cnt)
