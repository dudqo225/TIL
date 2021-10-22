import sys
sys.stdin = open('input.txt')

A, B = input().split()

num_list = [int(A[::-1]), int(B[::-1])]

print(max(num_list))

