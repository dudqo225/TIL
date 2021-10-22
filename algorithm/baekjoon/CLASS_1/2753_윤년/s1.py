import sys
sys.stdin = open('input.txt')

num = int(input())

# 윤년인 경우 1을 출력, 아닐 경우 0을 출력
# 윤년의 조건 : 4의 배수이면서, 100의 배수가 아니거나 400의 배수일 때
if num % 4 == 0 and (num % 100 or num % 400 == 0):
    print('1')
else:
    print('0')