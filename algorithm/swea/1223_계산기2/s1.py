import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    # 테스트 케이스 길이
    N = int(input())

    arr = input()

    stack = []
    result = ''
    
    # 후위표기법으로 변경
    for i in arr:
        if i in '0123456789':
            result += i
        if i == '+':
            while stack:
                result += stack.pop()
            stack.append(i)
        if i == '*':
            if stack:
                if stack[-1] == '*':
                    while stack and stack[-1] == '*':
                        result += stack.pop()
            stack.append(i)

    while stack:
        result += stack.pop()

    # print(result)
    stack = []

    for i in result:
        if i in '0123456789':
            stack.append(int(i))
        else:
            if i == '*':
                B = stack.pop()
                A = stack.pop()
                mul = A * B
                stack.append(mul)
            else:
                B = stack.pop()
                A = stack.pop()
                plus = A + B
                stack.append(plus)

    ans = stack.pop()
    print('#{} {}'.format(tc, ans))