import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    N = int(input())

    numbers = input()
    num_list = []
    for number in numbers:
        num_list.append(int(number))

    result = [0] * 10

    for num in num_list:
        result[num] += 1

    max_idx, max_num = 0, 0
    for i in range(len(result)-1, -1, -1):
        if result[i] > max_num:
            max_num = result[i]
            max_idx = i

    print('#{} {} {}'.format (TC, max_idx, max_num))