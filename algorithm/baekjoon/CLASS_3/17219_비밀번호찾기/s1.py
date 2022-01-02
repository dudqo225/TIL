import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

site = dict()

for _ in range(N):
    address, password = sys.stdin.readline().strip().split()

    site[address] = password

for _ in range(M):
    address = sys.stdin.readline().strip()
    print(site[address])