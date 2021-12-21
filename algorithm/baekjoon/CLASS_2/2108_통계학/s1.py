import sys
sys.stdin = open('input.txt')

from collections import Counter

N = int(input())

numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)

numbers.sort()
# 산술평균
ans_1 = round(sum(numbers) / N)

# 중앙값
ans_2 = numbers[N//2]

# 최빈값
cnt = Counter(numbers).most_common(2)

if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        ans_3 = cnt[1][0]
    else:
        ans_3 = cnt[0][0]
else:
    ans_3 = cnt[0][0]

# 범위
ans_4 = max(numbers) - min(numbers)

print(ans_1)
print(ans_2)
print(ans_3)
print(ans_4)
