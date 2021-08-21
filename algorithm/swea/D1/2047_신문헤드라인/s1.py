import sys
sys.stdin = open('input.txt')

text = input()

low_alpha = 'abcdefghijklmnopqrstuvwxyz'

result = ''
for i in text:
    if i in low_alpha:
        i = i.upper()
        result += i
    else:
        result += i

print(result)