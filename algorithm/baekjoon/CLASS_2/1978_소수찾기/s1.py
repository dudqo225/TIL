import sys
sys.stdin = open('input.txt')

'''
소수란?
1과 자기 자신 외의 약수를 가지지 않는 1보다 큰 자연수
'''

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

N = int(input())
n_list = list(map(int, input().split()))

ans = 0
for n in n_list:
    if n > 1:
        check = is_prime_number(n)
        if check == True:
            ans += 1

print(ans)