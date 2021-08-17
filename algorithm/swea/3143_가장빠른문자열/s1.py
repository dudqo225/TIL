import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    i = 0
    cnt = 0
    while i < len(A):
        if A[i:i+len(B)] == B:
            cnt += 1
            i = i + len(B)
        else:
            cnt += 1
            i += 1

    print('#{} {}'.format(tc, cnt))