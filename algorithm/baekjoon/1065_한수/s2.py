import sys
sys.stdin = open('input.txt')

N = int(input())

ans = 0
for i in range(1, N+1):
    if i < 100:
        ans += 1
    else:
        numbers = list(map(int, str(i)))
        if numbers[0] - numbers[1] == numbers[1] - numbers[2]:
            ans += 1

print(ans)
