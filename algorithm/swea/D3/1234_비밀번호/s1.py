import sys
sys.stdin = open('input.txt')

'''
while True로 반복문을 돌리고,
i, j 인덱스를 조정하여 문제를 해결하려 함.

but, i, j가 같은 위치에서 증/감 하는 보장이 없음.

틀린 코드임.
'''


T = 10
for tc in range(1, T+1):
    N, numbers = list(input().split())

    N = int(N)

    ans = numbers[:]

    print(ans)

    i = 0
    j = len(ans)-1
    print(j)
    while True:
        a = ans[i]
        b = ans[j]

        if a == b:
            i = 0
            j = len(ans)-1
            ans = ans[:i-1] + ans[j+1:]
        else:
            i += 1
            j -= 1

        if i > j:
            break

    print(ans)

