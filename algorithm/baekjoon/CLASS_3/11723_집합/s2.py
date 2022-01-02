import sys
sys.stdin = open('input.txt')

M = int(input())

S = set()
for _ in range(M):
    lst = sys.stdin.readline().strip().split()
    if len(lst) == 1:
        oper = lst[0]
        if oper == 'all':
            S = set([i for i in range(1, 21)])
        elif oper == 'empty':
            S = set()
    else:
        oper, x = lst[0], lst[1]
        x = int(x)
        if oper == 'add':
            S.add(x)
        elif oper == 'remove':
            S.discard(x)
        elif oper == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif oper == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)