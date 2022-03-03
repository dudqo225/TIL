import sys
sys.stdin = open('input.txt')

N = int(input())
stairs = []

for _ in range(N):
    stairs.append(int(input()))

dp = [stairs[0]]

for i in range(1, 3):
    if i == 1:
        dp.append(max(dp[i-1] + stairs[i], stairs[i]))
    else:
        dp.append(max(dp[i-2] + stairs[i], stairs[i-1] + stairs[i]))

for i in range(3, N):
    dp.append(max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i]))

print(dp[-1])