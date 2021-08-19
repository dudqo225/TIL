import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 T 입력
T = int(input())

# T만큼 반복
for tc in range(1, T+1):

    # 쇠막대기와 레이저 배치를 나타내는 괄호 표현 입력
    bar_list = input()
    
    # 쇠막대기 개수 bar, 잘린 쇠막대기 수 cut, 현재 쇠막대기 수 c_bar 변수 초기화
    bar = 0
    cut = 0
    c_bar = 0
    
    # bar_list 길이만큼 반복 순회
    for i in range(len(bar_list)):
        # i번째 인덱스가 '(' 일 경우
        if bar_list[i] == '(':
            # i+1번째 인덱스가 '(' 라면, 쇠막대기가 연결되는 것이므로 bar와 c_bar에 1씩 더해준다.
            if bar_list[i+1] == '(':
                bar += 1
                c_bar += 1
            # i+1번째 인덱스가 ')' 라면, 레이저이므로 cut에 현재 쇠막대기 수만큼 더해준다.
            else:
                cut += c_bar
        # i번째 인덱스가 ')' 일 경우        
        else:
            # i-1번째 인덱스가 ')' 일 경우, 쇠막대기 하나가 끝나는 지점이다.
            if bar_list[i-1] == ')':
                # 현재 쇠막대기 수 c_bar에서 1 빼준다.
                c_bar -= 1
    
    # result 변수에 총 쇠막대기 수 bar와 잘린 쇠막대기 수 cut을 더해준다.
    result = bar + cut
    
    # 결과 출력
    print('#{} {}'.format(tc, result))