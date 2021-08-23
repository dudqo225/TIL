import sys
sys.stdin = open('input.txt')

'''
문제
주어진 숫자부터 0까지 순서대로 찍어보세요
'''

N = int(input())

for i in range(N, -1, -1):
    print(i, end=' ')