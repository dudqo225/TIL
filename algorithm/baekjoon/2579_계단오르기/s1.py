import sys
sys.stdin = open('input.txt')


def check(total, idx, limit):
    global ans_list

    if limit == 3:
        return
    if idx == N-1:
        ans_list.append(total)
        return

    for i in range(idx+1, N):
        limit += 1
        check(total + stairs[i], i, limit)
        limit = 1


N = int(input())
stairs = []

for _ in range(N):
    stairs.append(int(input()))

ans_list = []
for i in range(2):
    check(stairs[i], 0, 1)

print(max(ans_list))