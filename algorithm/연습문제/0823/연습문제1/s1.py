import sys
sys.stdin = open('input.txt')

arr = input()

stack = []
result = ''

for i in arr:
    if i in '+-*/':
        stack.append(i)
    else:
        result += i

while stack:
    result += stack.pop()

print(result)