import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    cards = list(input().split())
    
    ans = []

    # 홀수
    if len(cards) % 2:
        first = cards[0:(len(cards)//2)+1]
        second = cards[(len(cards)//2)+1:]

        while second:
            temp1 = first.pop(0)
            temp2 = second.pop(0)

            ans.append(temp1)
            ans.append(temp2)
        ans.append(first.pop(0))

    # 짝수
    else:
        first = cards[0:(len(cards)//2)]
        second = cards[(len(cards)//2):]

        while first:
            temp1 = first.pop(0)
            temp2 = second.pop(0)

            ans.append(temp1)
            ans.append(temp2)

    print('#{}'.format(tc), end=' ')
    print(*ans, sep=' ')