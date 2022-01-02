import sys
sys.stdin = open('input.txt')

M = int(input())

S = [0 for i in range(20)]
for _ in range(M):
    lst = list(input().split())
    if len(lst) == 1:
        oper = lst[0]
        if oper == 'all':
            S = [1 for i in range(20)]
        elif oper == 'empty':
            S = [0 for i in range(20)]
    else:
        oper, x = lst[0], lst[1]
        x = int(x)
        if oper == 'add':
            if not S[x-1]:
                S[x-1] = 1
        elif oper == 'remove':
            if S[x-1]:
                S[x-1] = 0
        elif oper == 'check':
            if S[x-1]:
                print(1)
            else:
                print(0)
        elif oper == 'toggle':
            if S[x-1]:
                S[x-1] = 0
            else:
                S[x-1] = 1