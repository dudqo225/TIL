import sys
sys.stdin = open('input.txt')

'''
소인수분해
- 소수인 인수들만의 곱으로 나타내는 수

문제 조건
- 2, 3, 5, 7, 11 등 5가지 소수로 나타나는 숫자 N에 대해서,
각 a, b, c, d, e를 출력하라.

풀이
- 숫자 N을 작은 소수부터 나눈다.
N을 소수로 나누어 0으로 떨어지는 동안 while문과 if문을 반복하고,
0으로 나누어 떨어지지 않으면 그 다음 소수로 넘어가서 위 반복을 시행한다.
'''

T = int(input())
for tc in range(1, T+1):
    # 소수 리스트
    num_list = [2, 3, 5, 7, 11]
    # 입력받은 숫자 N
    N = int(input())

    # a, b, c, d, e를 저장하는 리스트
    ans = [0] * 5

    # i=0 부터 시작
    i = 0
    # 입력받는 숫자 N이 1이 될때까지 반복문 수행
    while N > 1:
        # N이 i번째 소수로 나누어 떨어지면,
        if N % num_list[i] == 0:
            # ans 리스트의 i번째 값을 1 증가
            ans[i] += 1
            # N을 i번째 소수로 나눈 값을 재할당
            N //= num_list[i]
        # N이 i번째 소수로 나누어 떨어지지 않으면, i를 1 증가
        else:
            i += 1

    # 결과 출력
    print('#{}'.format(tc), end=' ')
    print(*ans)
