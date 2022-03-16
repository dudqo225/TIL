import sys
from collections import deque

sys.stdin = open('input.txt')

brackets = input()

q = deque()
check = True

if brackets[0] in [')', ']']:
    check = False

for bracket in brackets:
    if not check:
        break

    if bracket == '(' or bracket == '[':
        q.append(bracket)

    elif bracket == ')' and q:
        if q[-1] == '(':
            q.pop()
            q.append(2)
        elif q[-1] == '[':
            check = False
        else:
            val = 0
            while q:
                ext = q.pop()
                if ext == '(':
                    val *= 2
                    q.append(val)
                    break
                elif ext == '[':
                    check = False
                    break
                else:
                    val += ext

    elif bracket == ']' and q:
        if q[-1] == '[':
            q.pop()
            q.append(3)
        elif q[-1] == '(':
            check = False
        else:
            val = 0
            while q:
                ext = q.pop()
                if ext == '[':
                    val *= 3
                    q.append(val)
                    break
                elif ext == '(':
                    check = False
                    break
                else:
                    val += ext

    else:
        q.append(bracket)

ans = 0
if not check:
    print(ans)
else:
    for i in q:
        if i in ['(', ')', '[', ']']:
            ans = 0
            break
        else:
            ans += i
    print(ans)