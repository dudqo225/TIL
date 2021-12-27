import sys
sys.stdin = open('input.txt')

from collections import deque

while True:
    parentheses = ['(', ')', '[', ']']
    stop = False

    words = sys.stdin.readline()
    if words == '.':
        break
    parenthesis_list = deque()

    for word in words:
        if word in parentheses:
            parenthesis_list.append(word)

    if parenthesis_list and (parenthesis_list[0] == ')' or parenthesis_list[0] == ']'):
        print('no')
        continue

    while parenthesis_list:
        if (parenthesis_list[0] == '(' and parenthesis_list[1] == ')') or (parenthesis_list[0] == '[' and parenthesis_list[1] == ']'):
            parenthesis_list.popleft()
            parenthesis_list.popleft()
        elif (parenthesis_list[0] == '(' and parenthesis_list[1] == ']') or (parenthesis_list[0] == '[' and parenthesis_list[1] == ')'):
            print('no')
            stop = True
            break
        else:
            temp = parenthesis_list.popleft()
            parenthesis_list.append(temp)

    if stop:
        continue

    print('yes')