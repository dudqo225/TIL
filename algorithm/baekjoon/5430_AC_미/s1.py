import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    p = input()
    n = int(input())
    numbers = input()
    print(numbers)