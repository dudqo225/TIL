import sys
sys.stdin = open('input.txt')

from itertools import permutations


def check(lst):
    total = 0

    for i in range(len(lst)):
        total += lst[i] * B[i]

        if total >= ans:
            return False

    return total


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 9876543210

combi = set(permutations(A, N))
for comb in combi:
    res = check(comb)

    if type(res) == bool:
        continue
    else:
        if res < ans:
            ans = res

print(ans)