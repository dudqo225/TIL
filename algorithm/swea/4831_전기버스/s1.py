import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    charge_station = list(map(int, input().split()))
    count = current = 0

    while current + K < N:
        for step in range(K, 0, -1):
            if (current + step) in charge_station:
                current += step
                count += 1
                break
        else:
            count = 0
            break


    print('#{0} {1}'.format(TC, count))
