import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    computer = a ** b
    ans = str(computer)[-1]

    print(ans)
