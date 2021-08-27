import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())

    stack = []

    for i in arr:
        if i.isnumeric():
            stack.append(int(i))
        elif i == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
            break
        else:
            if len(stack) >= 2:
                B = stack.pop()
                A = stack.pop()

                if i == '+':
                    stack.append(A + B)
                if i == '-':
                    stack.append(A - B)
                if i == '*':
                    stack.append(A * B)
                if i == '/':
                    stack.append(A // B)
            else:
                result = 'error'
                break

    print('#{} {}'.format(tc, result))