import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    ps = list(input())
    length = len(ps)
    first = ps.pop(0)

    if first == '(':
        left = [first]
    else:
        print('NO')
        continue

    i = 1
    while i < length:
        temp = ps.pop(0)
        if temp == '(':
            left.append(temp)
        elif temp == ')' and left:
            left.pop()
        else:
            left.append(temp)
        i += 1

    if left:
        ans = 'NO'
    else:
        ans = 'YES'

    print(ans)