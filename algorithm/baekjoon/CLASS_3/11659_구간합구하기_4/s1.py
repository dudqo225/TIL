import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

accumulate_lst = [0]
total = 0

for number in numbers:
    total += number
    accumulate_lst.append(total)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    ans = accumulate_lst[j] - accumulate_lst[i-1]
    print(ans)