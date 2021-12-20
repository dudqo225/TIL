import sys
sys.stdin = open('input.txt')

n = int(input())

stack = []
ans = []
cnt = 0

no_answer = True

for i in range(n):
    x = int(input())

    while cnt < x:
        cnt += 1
        stack.append(cnt)
        ans.append('+')

    if stack[-1] == x:
        stack.pop()
        ans.append('-')
    else:
        no_answer = False
        break

if no_answer == False:
    print('NO')
else:
    print('\n'.join(ans))