import sys
sys.stdin = open('input.txt')

'''
문제 조건에 맞게 재귀를 활용한 코드

재귀
- base case와 그 외 case를 구분하여 코드를 작성
- 코드 안에 정의된 함수를 재활용하는 성격을 가지고 있다.
'''

# 거듭제곱 재귀 함수 코드
def power(a, b):
    # base case
    if b == 0:
        return 1
    # 그 외
    else:
        return a * power(a, b-1)

T = 10
for tc in range(1, T+1):
    tc_num = int(input())
    N, M = map(int, input().split())

    ans = power(N, M)

    print('#{} {}'.format(tc_num, ans))