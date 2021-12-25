import sys
sys.stdin = open('input.txt')

def prime_list(m, n):
    sieve = [True] * (n+1)
    if m == 1:
        sieve[1] = False

    for i in range(2, int(n**0.5)+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return [i for i in range(m, n+1) if sieve[i] == True]

M, N = map(int, input().split())

ans = prime_list(M, N)

for a in ans:
    print(a)