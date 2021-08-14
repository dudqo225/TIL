import sys
sys.stdin = open('input.txt')

def strNumberSort(arr):

    # str 숫자를 int 숫자로 바꾸기
    num_list = []
    for i in arr:
        if i == 'ZRO':
            num_list.append(0)
        elif i == 'ONE':
            num_list.append(1)
        elif i == 'TWO':
            num_list.append(2)
        elif i == 'THR':
            num_list.append(3)
        elif i == 'FOR':
            num_list.append(4)
        elif i == 'FIV':
            num_list.append(5)
        elif i == 'SIX':
            num_list.append(6)
        elif i == 'SVN':
            num_list.append(7)
        elif i == 'EGT':
            num_list.append(8)
        elif i == 'NIN':
            num_list.append(9)

    # 숫자 정렬하기
    for i in range(len(num_list)-1, 0, -1):
        for j in range(0, i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    # int 숫자를 다시 str 숫자로 바꾸기
    result = []
    for num in num_list:
        if num == 0:
            result.append('ZRO')
        elif num == 1:
            result.append('ONE')
        elif num == 2:
            result.append('TWO')
        elif num == 3:
            result.append('THR')
        elif num == 4:
            result.append('FOR')
        elif num == 5:
            result.append('FIV')
        elif num == 6:
            result.append('SIX')
        elif num == 7:
            result.append('SVN')
        elif num == 8:
            result.append('EGT')
        elif num == 9:
            result.append('NIN')

    return result

# 테스트 케이스 개수 T 입력
T = int(input())

# T만큼 반복
for tc in range(1, T+1):
    # 테스트 케이스 번호와 테스트 케이스의 길이 입력
    tc_num, tc_length = map(str, input().split())

    # 테스트 케이스 문자열 입력
    arr = list(map(str, input().split()))

    # 결과 출력
    print('#{}'.format(tc))
    for i in strNumberSort(arr):
        print(i, end=' ')
    print()