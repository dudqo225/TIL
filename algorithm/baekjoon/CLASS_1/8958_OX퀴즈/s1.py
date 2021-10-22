import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = input()

    total = 0
    cnt = 0

    for i in arr:
        if i == 'O':
            cnt += 1
            total += cnt
        else:
            cnt = 0

    print(total)