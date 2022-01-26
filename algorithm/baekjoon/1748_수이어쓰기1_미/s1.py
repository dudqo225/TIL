import sys
sys.stdin = open('input.txt')

N = int(input())

conn = 0

for i in range(1, N+1):
    conn += len(str(i))

print(conn)