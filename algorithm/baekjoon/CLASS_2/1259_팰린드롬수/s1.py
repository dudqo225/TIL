import sys
sys.stdin = open('input.txt')

def findPalindrome(num):

    num_str = str(num)
    if num_str == num_str[::-1]:
        return 'yes'
    else:
        return 'no'

while True:
    num = int(input())
    if num == 0:
        break
    else:
        print(findPalindrome(num))



