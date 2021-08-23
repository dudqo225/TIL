import sys
sys.stdin = open('input.txt')

'''
문제
입력으로 1개의 정수 N이 주어진다.
정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

제약사항
N은 1이상 1000이하의 정수이다.

입력
정수 N

출력
정수 N의 모든 약수를 오름차순으로 출력
'''

N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')