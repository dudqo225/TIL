import sys
sys.stdin = open('input.txt')

T = int(input())

def subsetSum(arr, n):

    for i in range(1<<n):
        total = 0
        for j in range(n):
            if i & (1<<j):
                total += arr[j]
                if total == 0:
                    return 1
    else:
        return 0


for TC in range(1, T+1):
    arr = list(map(int, input().split()))

    n = len(arr)
    print('#{0} {1}'.format(TC, subsetSum(arr, n)))



