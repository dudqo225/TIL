import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    lst = [10,
           1,
           [2, 4, 8, 6],
           [3, 9, 7, 1],
           [4, 6],
           5,
           6,
           [7, 9, 3, 1],
           [8, 4, 2, 6],
           [9, 1]]

    x = int(str(a)[-1])
    if x == 0:
        ans = 10
    elif x in [1, 5, 6]:
        ans = x
    elif x in [2, 3, 7, 8]:
        ans = lst[x][b%4-1]
    else:
        if b % 2 == 0:
            ans = lst[x][1]
        else:
            ans = lst[x][0]

    print(ans)