import sys
sys.stdin = open('input.txt')

lst = list(input())

for i in range(len(lst)):
    print(ord(lst[i])-64, end=' ')

