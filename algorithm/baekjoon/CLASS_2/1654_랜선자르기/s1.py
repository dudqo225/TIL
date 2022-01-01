import sys
sys.stdin = open('input.txt')

K, N = map(int, input().split())

cables = []

for _ in range(K):
    cable = int(input())
    cables.append(cable)

start = 1
end = max(cables)
ans = 0

while start <= end:
    cnt = 0

    mid = (start + end) // 2

    for cable in cables:
        if cable >= mid:
            cnt += cable // mid

    if cnt >= N:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)