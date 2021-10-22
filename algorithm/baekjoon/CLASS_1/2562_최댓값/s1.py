import sys

sys.stdin = open('input.txt')

N = 9

num_list = []

for _ in range(N):
    num = int(input())
    num_list.append(num)

print(max(num_list))
print(num_list.index(max(num_list))+1)