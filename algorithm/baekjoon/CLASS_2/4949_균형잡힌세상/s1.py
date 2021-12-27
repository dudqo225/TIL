import sys
sys.stdin = open('input.txt')

parentheses = ['(', ')', '[', ']']

while True:
    stop = False

    words = input()
    if words == '.':
        break

    small = 0
    big = 0

    for word in words:
        if word == '(':
            small += 1
        elif word == ')':
            small -= 1
        elif word == '[':
            big += 1
        elif word == ']':
            big -= 1

        if small < 0 or big < 0:
            print('no' + str(i))
            stop = True
            break
    if stop:
        continue

    if small > 0 or big > 0:
        print('no' + str(i))
    elif small == 0 and big == 0:
        print('yes' + str(i))