import sys
sys.stdin = open('input.txt')

# 괄호의 짝이 유효한지 확인하는 함수. s는 문자열
def bracSearch(s):

    # 소, 중괄호 포함 여부를 확인하기 위해 리스트 생성
    bracket_list = ['{', '}', '(', ')']

    # 빈 stack 생성
    stack = []

    # 문자열 s를 반복 순회
    for char in s:
        # char이 괄호 리스트에 있는지 확인
        if char in bracket_list:
            # 현재 stack이 비어있지 않을 경우
            if stack:
                # stack의 마지막 값과 char 쌍의 짝이 맞다면, stack에서 제거
                if (stack[-1] == '{' and char == '}') or (stack[-1] == '(' and char == ')'):
                    stack.pop()
                # 짝이 맞지 않다면, stack에 char 추가
                else:
                    stack.append(char)
            # 현재 stack이 비어있다면, stack에 char 추가
            else:
                stack.append(char)

    # stack이 비어있지 않다면, 정상적으로 짝을 이룬 것이 아니므로 0을 반환
    if stack:
        return 0
    # stack이 비어있다면, 정상적으로 짝을 이루었으므로 1을 반환
    else:
        return 1

# 테스트 케이스 개수 T 입력
T = int(input())

# T만큼 반복
for tc in range(1, T+1):

    # 문자열 s 입력
    s = input()

    # 결과 출력
    print('#{} {}'.format(tc, bracSearch(s)))