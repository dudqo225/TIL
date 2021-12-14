import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    money = int(input())

    ans = []

    cost = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for i in range(len(cost)):
        if money >= cost[i]:
            ans.append(money//cost[i])
            money -= money//cost[i] * cost[i]
        else:
            ans.append(0)

    print('#{}'.format(tc))
    print(*ans)