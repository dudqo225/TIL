import sys
sys.stdin = open('input.txt')

# 테스트 케이스는 10
T = 10

# 10번 반복
for tc in range(1, T+1):
    # 테스트 케이스 번호 입력
    tc_num = int(input())

    # 찾을 문자열과 검색할 문장 입력
    p = input()
    t = input()

    # 특정 문자열 개수를 세는 변수 생성
    cnt = 0
    
    # 검색할 문장의 길이만큼 반복 수행
    for i in range(len(t)):
        # 찾을 문자열 첫번째와 검색할 문장의 i 인덱스 값이 같고
        if t[i] == p[0]:
            # 검색할 문장 i부터 찾을 문자열 길이만큼의 값이 p와 같다면
            if t[i:i+len(p)] == p:
                # cnt 에 1을 더해준다
                cnt += 1
    
    # 결과 출력
    print('#{} {}'.format(tc, cnt))