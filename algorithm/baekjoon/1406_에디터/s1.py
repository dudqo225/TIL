import sys
sys.stdin = open('input.txt')

words = sys.stdin.readline().rstrip()
N = len(words)

M = int(input())

for _ in range(M):
    command = list(sys.stdin.readline().split())

    if command[0] == 'P':
        words = words[:N] + command[1] + words[N:]
        N += 1
    elif command[0] == 'L':
        if N != 0:
            N -= 1
    elif command[0] == 'D':
        if N != len(words):
            N += 1
    elif command[0] == 'B':
        if N != 0:
            words = words[:N-1] + words[N:]
            N -= 1

print(words)