import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

print(numbers)