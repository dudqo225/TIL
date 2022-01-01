# import sys
# sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pocketmon_list = []
pocketmon_dict = {}

for i in range(N):
    pocketmon = input().rstrip()
    pocketmon_list.append(pocketmon)
    pocketmon_dict[pocketmon] = i+1

for i in range(M):
    val = input().rstrip()
    if val.isalpha():
        print(pocketmon_dict[val])
    else:
        print(pocketmon_list[int(val)-1])