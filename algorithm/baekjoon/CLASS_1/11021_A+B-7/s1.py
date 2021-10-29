import sys
sys.stdin = open('input.txt')

# 백준 제출용
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    print('Case #{}: {}'.format(tc, A+B))