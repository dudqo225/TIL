import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    dic = {}
    for char in str1:
        dic[char] = 0

    for char in str2:
        if char in dic:
            dic[char] += 1

    result = max(dic.values())

    print('#{} {}'.format(tc, result))