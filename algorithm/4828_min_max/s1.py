import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number
        elif number < min_value:
            min_value = number

    result = max_value - min_value
    print('#{} {}'.format(i+1, result))