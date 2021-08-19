import sys
sys.stdin = open('input.txt')

# 반복문자를 제거하는 함수 dupStr
def dupStr(s):

    # s의 0번째를 시작점으로 stack에 넣고 시작
    stack = [s[0]]

    # 1부터 문자열 s 길이만큼 반복
    for i in range(1, len(s)):
        # stack이 비어있지 않다면
        if stack:
            # stack의 마지막 값과 s의 i번째 값을 비교해서 같으면
            if stack[-1] == s[i]:
                # pop()을 통해 중복값 제거
                stack.pop()
            # 같지 않다면 stack에 s의 i번째 값을 추가
            else:
                stack.append(s[i])
        # 현재 stack이 비어있다면, stack에 s의 i번째 값을 추가
        else:
            stack.append(s[i])
    
    # 남은 문자열이 있으면, stack의 길이를 리턴
    if len(stack):
        return len(stack)
    # 남은 문자열이 없으면, 0을 리턴
    else:
        return 0

# 테스트 케이스 T 개수 입력
T = int(input())

# T만큼 반복
for tc in range(1, T+1):

    # 문자열 s 입력
    s = input()
    
    # 결과 출력
    print('#{} {}'.format(tc, dupStr(s)))
