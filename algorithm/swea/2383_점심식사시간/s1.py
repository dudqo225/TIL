import sys
sys.stdin = open('input.txt')

# 기본 테케 및 input 받아오기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range (N)]