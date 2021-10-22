import sys
sys.stdin = open('input.txt')

num_list = [int(input()) for _ in range(10)]

for i in range(len(num_list)):
    num_list[i] = num_list[i] % 42

ans = len(set(num_list))

print(ans)