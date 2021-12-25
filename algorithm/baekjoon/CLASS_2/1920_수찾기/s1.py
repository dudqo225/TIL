import sys
sys.stdin = open('input.txt')

'''
Python3 로 채점하면 시간초과.
PyPy3 로 채점하면 통과...
'''

N = int(input())
a_list = list(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))

for m in m_list:
    if m in a_list:
        print(1)
    else:
        print(0)