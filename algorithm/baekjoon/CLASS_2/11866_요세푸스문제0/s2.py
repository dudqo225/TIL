import sys
sys.stdin = open('input.txt')

from collections import deque

N, K = map(int, input().split())

Q = deque()
ans = []

for i in range(1, N+1):
    Q.append(i)

while Q:
    for i in range(K-1):
        Q.append(Q[0])
        Q.popleft()
    ans.append(Q.popleft())

print('<', end='')
for i in range(len(ans)-1):
    print('{}, '.format(ans[i]), end='')
print('{}>'.format(ans[-1]))