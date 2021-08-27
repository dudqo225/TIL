import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    # N은 테스트 케이스의 길이
    N = int(input())
    # 테스트를 입력받아 arr에 저장
    arr = input()

    # 후위 표기식으로 변경
    # 우선순위 딕셔너리 icp, isp 생성
    
    icp = {
        '+': 1,
        '*': 2,
        '(': 3,
    }
    isp = {
        '(': 0,
        '+': 1,
        '*': 2,
    }
    
    # 연산자를 저장하기 위한 스택 리스트 생성
    stack = []
    # 후위 표기식으로 변경되는 결과를 저장하는 변수 생성
    result = ''
    # arr를 반복 순회한다.
    for i in arr:
        # i 가 피연산자일 경우 result 에 i를 추가
        if i in '0123456789':
            result += i
        # i 가 + or * 연산자일 경우
        elif i in '+*':
            # 스택이 비어있다면, stack에 i를 추가
            if not stack:
                stack.append(i)
            # 비어있지 않을 경우
            else:
                # i의 icp가 스택 top의 isp보다 크면 stack에 i를 추가
                if icp[i] > isp[stack[-1]]:
                    stack.append(i)
                # i의 icp가 스택 top의 isp보다 작다면
                else:
                    # 스택 top의 isp가 i의 icp보다 작아질 때까지 스택에서 pop하여 result에 추가
                    while isp[stack[-1]] > icp[i]:
                        result += stack.pop()
                    stack.append(i)
        # i가 여는 괄호일 경우 stack에 추가
        elif i == '(':
            stack.append(i)
        # i가 닫는 괄호일 경우
        else:
            # 스택의 마지막 값이 여는 괄호가 될 때까지 스택에서 pop하여 result에 추가
            while stack[-1] != '(':
                result += stack.pop()
            # 스택의 마지막 값이 여는 괄호가 되어서 반복문이 종료되면, 여는 괄호를 삭제
            stack.pop()
    
    # arr 반복 순회 이후, stack에 남아있는 연산자가 있으면 모두 pop하여 result에 추가
    while stack:
        result += stack.pop()

    # 후위 표기식 계산하기
    stack = []

    for i in result:
        if i in '0123456789':
            stack.append(int(i))
        else:
            if len(stack) >= 2:
                B = stack.pop()
                A = stack.pop()

                if i == '+':
                    stack.append(A + B)
                if i == '*':
                    stack.append(A * B)

    ans = stack[-1]

    print('#{} {}'.format(tc, ans))