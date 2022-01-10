import sys
from collections import deque
sys.stdin = open('input.txt')

words = deque(sys.stdin.readline().rstrip())
N = len(words)
M = int(input())

words2 = deque()

for _ in range(M):
    command = list(sys.stdin.readline().split())

    if command[0] == 'P':
        words.append(command[1])
    elif command[0] == 'L' and words:
        words2.appendleft(words.pop())
    elif command[0] == 'D' and words2:
        words.append(words2.popleft())
    elif command[0] == 'B' and words:
        words.pop()

print(''.join(words + words2))