import sys
sys.stdin = open('input.txt')

while True:
    words = input()
    if words == '.':
        break

    stack = []

    for word in words:
        if word == '(' or word == '[':
            stack.append(word)
        elif word == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(word)
                break
        elif word == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(word)
                break

    if stack:
        print('no')
    else:
        print('yes')