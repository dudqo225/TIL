import sys

sys.stdin = open('input.txt')

num_1 = int(input())
num_2 = input()

print(num_1*int(num_2[2]))
print(num_1*int(num_2[1]))
print(num_1*int(num_2[0]))
print(num_1*int(num_2))
