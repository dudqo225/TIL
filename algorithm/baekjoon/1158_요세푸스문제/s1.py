import sys
sys.stdin = open('input.txt')

from collections import deque

N, K = map(int, sys.stdin.readline().split())

numbers = deque(range(1, N+1))
ans = deque()

while numbers:
    i = 1
    while i != K:
        numbers.append(numbers.popleft())
        i += 1
    ans.append(numbers.popleft())

print('<', end='')
for i in range(N-1):
    print(ans[i], end=', ')
print('{}>'.format(ans[-1]))