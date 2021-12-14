import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    times = list(map(int, input().split()))

    hours = times[0] + times[2]
    minutes = times[1] + times[3]

    if minutes >= 60:
        minutes -= 60
        hours += 1
    if hours >= 12:
        hours -= 12

    print('#{} {} {}'.format(tc, hours, minutes))