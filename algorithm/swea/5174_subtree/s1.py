import sys
sys.stdin = open('input.txt')

def subTree(x):
    global cnt

    if x == 0:
        return

    cnt += 1
    subTree(left[x])
    subTree(right[x])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())

    arr = list(map(int, input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i+1]
        if left[parent]:
            right[parent] = child
        else:
            left[parent] = child

    cnt = 0
    subTree(N)

    print('#{} {}'.format(tc, cnt))