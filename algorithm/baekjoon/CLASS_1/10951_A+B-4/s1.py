import sys

sys.stdin = open('input.txt')

'''
입력받는 테스트 케이스 개수가 명시되어 있지 않기 때문에
while 구문과 try-except 문을 통해서 결과를 출력한다.
'''

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break