import sys
sys.stdin = open('input.txt')

def binary_search(n, key):
    global ans

    l = 0
    r = len(n)-1
    check = ''

    while l <= r:
        mid = (l + r) // 2
        if n[mid] == key:
            ans += 1
            break

        elif n[mid] > key:
            r = mid - 1
            now = 'left'

        else:
            l = mid + 1
            now = 'right'

        if check == now:
            break

        check = now
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_arr = sorted(list(map(int, input().split())))
    M_arr = list(map(int, input().split()))

    ans = 0
    for num in M_arr:
        binary_search(N_arr, num)

    print('#{} {}'.format(tc, ans))