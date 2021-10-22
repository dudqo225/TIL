import sys

sys.stdin = open('input.txt')

'''
입력받는 테스트 케이스의 마지막에 0이 두 개가 들어오기 때문에
while문을 반복하다가, 0, 0을 만나면 break 되게끔 조건을 걸어준다.
'''

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A + B)
