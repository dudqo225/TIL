import sys
sys.stdin = open('input.txt')

# 테스트 케이스 T 입력
T = int(input())
for tc in range(1, T+1):
    # N : 숫자 개수 / M : 작업 횟수
    N, M = map(int, input().split())

    # 숫자 리스트 입력
    numbers = list(map(int, input().split()))

    # 작업 횟수 M만큼 반복
    for _ in range(M):
        temp = numbers.pop(0)
        numbers.append(temp)

    # 수열의 맨 앞에 있는 숫자를 result에 저장
    result = numbers[0]

    # 결과 출력
    print('#{} {}'.format(tc, result))