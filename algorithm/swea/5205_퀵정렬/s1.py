import sys
sys.stdin = open('input.txt')

def quick_sort(arr, left, right):
    if left < right:
        s = partition(arr, left, right)
        quick_sort(arr, left, s-1)
        quick_sort(arr, s+1, right)

def partition(arr, left, right):
    pivot = arr[left]
    i = left
    j = right
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N-1)
    ans = arr[N//2]

    print('#{} {}'.format(tc, ans))