import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = list(sys.stdin.readline().split())

    ans = []

    for word in words:
        ans.append(word[::-1])

    print(' '.join(ans))