import sys
sys.stdin = open('input.txt')

cro_alpha = input()

i = 0
ans = 0
while i <= len(cro_alpha)-1:
    if cro_alpha[i] == 'c':
        if cro_alpha[i+1] == '=' or cro_alpha[i+1] == '-':
            i += 2
            ans += 1
        else:
            i += 1
            ans += 1
    elif cro_alpha[i] == 'd':
        if cro_alpha[i+1] == 'z':
            if cro_alpha[i+2] == '=':
                i += 3
                ans += 1
            else:
                ans += 2
        elif cro_alpha[i+1] == '-':
            i += 2
            ans += 1
        else:
            i += 1
            ans += 1
    elif cro_alpha[i] == 'l' or cro_alpha[i] == 'n':
        if cro_alpha[i+1] == 'j':
            i += 2
            ans += 1
        else:
            i += 1
            ans += 1
    elif cro_alpha[i] == 's' or cro_alpha[i] == 'z':
        if cro_alpha[i+1] == '=':
            i += 2
            ans += 1
        else:
            i += 1
            ans += 1
    else:
        i += 1
        ans += 1

print(ans)