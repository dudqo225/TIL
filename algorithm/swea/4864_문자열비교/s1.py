import sys
sys.stdin = open('input.txt')


def bruteForce(p, t):
    '''
    고지식한 알고리즘으로, 본문 문자열을 처음부터 끝까지 차례대로 순회하면서
    패턴 내의 문자들을 일일이 비교하는 함수.
    '''

    N = len(t)  # 전체 텍스트의 길이
    M = len(p)  # 찾을 패턴의 길이

    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    
    # 인덱스 범위 내에서 반복
    while j < M and i < N:
        # 텍스트의 i번째 인덱스와 패턴의 j번째 인덱스가 다를 경우
        if t[i] != p[j]:
            # 비교를 시작한 위치로 돌아간다
            i = i - j
            # j는 초기화
            j = -1
        # i와 j에 1씩 더해준다            
        i += 1
        j += 1
    
    # j와 패턴의 길이 M이 일치하면, 검색에 성공한 것이기 때문에 1을 return
    if j == M:
        return 1
    # 검색에 실패한 경우, 0을 return
    else:
        return 0

# 테스트 케이스 개수 T 입력
T = int(input())

# T만큼 반복
for tc in range(1, T+1):
    
    # 찾을 패턴 p와 전체 텍스트 t를 입력
    p = input()
    t = input()
    
    # 결과 출력
    print('#{} {}'.format(tc, bruteForce(p, t)))


