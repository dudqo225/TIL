import sys
from collections import deque

sys.stdin = open('input.txt')

brackets = input()
q = deque()
ans = 0
tmp = 1

for i in range(len(brackets)):
    if brackets[i] == '(':
        tmp *= 2
        q.append(brackets[i])

    elif brackets[i] == '[':
        tmp *= 3
        q.append(brackets[i])

    elif brackets[i] == ')':
        if q[-1] == '[' or not q:
            ans = 0
            break
        if

    elif brackets[i] == ']':
        pass

ans = 0
if not check:
    print(0)
else:
    for i in q:
        if i in ['(', ')', '[', ']']:
            ans = 0
            break
        else:
            ans += i
    print(ans)
