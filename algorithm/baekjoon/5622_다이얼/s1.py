import sys
sys.stdin = open('input.txt')

alpha_list = input()
ans = 0

for alpha in alpha_list:
    if alpha in 'ABC':
        ans += 3
    elif alpha in 'DEF':
        ans += 4
    elif alpha in 'GHI':
        ans += 5
    elif alpha in 'JKL':
        ans += 6
    elif alpha in 'MNO':
        ans += 7
    elif alpha in 'PQRS':
        ans += 8
    elif alpha in 'TUV':
        ans += 9
    elif alpha in 'WXYZ':
        ans += 10

print(ans)