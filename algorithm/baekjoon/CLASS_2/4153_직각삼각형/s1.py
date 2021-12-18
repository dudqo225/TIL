import sys
sys.stdin = open('input.txt')

while True:
    numbers = list(map(int, input().split()))

    # 마지막 입력값이 0, 0, 0 일 경우 반복문 break
    if sum(numbers) == 0:
        break

    # 입력받은 numbers 리스트에서 최대값 찾기
    c = max(numbers)
    # 찾은 최대값을 numbers 리스트에서 제거
    numbers.remove(c)

    # 피타고라스 정리 > a ** 2 + b ** 2 = c ** 2
    if numbers[0] ** 2 + numbers[1] ** 2 == c ** 2:
        ans = 'right'
    else:
        ans = 'wrong'

    print(ans)