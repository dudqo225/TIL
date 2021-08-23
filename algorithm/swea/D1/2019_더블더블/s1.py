import sys
sys.stdin = open('input.txt')

'''
문제
1부터 주어진 횟수까지 2를 곱한 값을 출력하시오.
주어질 숫자는 30을 넘지 않는다.
'''

N = int(input())

x = 1
print(x, end=' ')

for i in range(N):
    x = x * 2
    print(x, end=' ')
