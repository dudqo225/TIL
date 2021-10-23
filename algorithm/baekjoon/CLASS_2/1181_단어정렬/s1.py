import sys
sys.stdin = open('input.txt')

N = int(input())

res = []
for _ in range(N):
    a = input()
    if a not in res:
        res.append(a)

# 한번 정렬하면 알파벳순으로 정렬됨.
res.sort()
# len(길이)를 key로 정렬하면 이미 알파벳순으로 정렬된 리스트가 다시 길이순으로 졍렬된다.
res.sort(key=len)

for r in res:
    print(r)
