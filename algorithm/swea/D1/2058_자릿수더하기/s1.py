import sys
sys.stdin = open('input.txt')

# 자연수 N 입력
N = int(input())

# 각 자릿수 합을 저장하는 result 변수 초기화
result = 0

# N이 0보다 큰 동안 반복
while N > 0:
    # result 에 N을 10으로 나눈 나머지를 저장
    result += N % 10
    # N에 N을 10으로 나눈 몫을 새로 할당
    N = N // 10

# 결과 출력
print(result)


