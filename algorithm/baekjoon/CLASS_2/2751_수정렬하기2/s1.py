import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

# 버블정렬
# for i in range(N-1, 0, -1):
#     for j in range(0, i):
#         if num_list[j] > num_list[j+1]:
#             num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
#
# print(*num_list, sep='\n')

# 퀵정렬
def quicksort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quicksort(a, begin, p-1)
        quicksort(a, p+1, end)

def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(L < R and a[L] < a[pivot]): L += 1
        while(L < R and a[R] > a[pivot]): R -= 1
        if L < R:
            if L == pivot: pivot = R
            a[L], a[R] = a[R], a[L]

    a[pivot], a[R] = a[R], a[pivot]
    return R

quicksort(num_list, 0, N-1)

print(*num_list, sep='\n')