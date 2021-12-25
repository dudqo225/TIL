import sys
sys.stdin = open('input.txt')

# 최대공약수
def GCD_MOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

# 최소공배수
def LCM(a, b, gcd):
    return a * b // gcd

A, B = map(int, input().split())

gcd = GCD_MOD(A, B)
lcm = LCM(A, B, gcd)

print(gcd)
print(lcm)