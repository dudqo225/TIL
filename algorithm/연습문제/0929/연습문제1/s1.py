import sys
sys.stdin = open('input.txt')

str_num = input()

result = []
for i in range(0, len(str_num), 7):
    temp = str_num[i:i+7]
    result.append(str(int(temp, 2)))

print(', '.join(result))
