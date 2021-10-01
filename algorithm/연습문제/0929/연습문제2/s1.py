import sys
sys.stdin = open('input.txt')

# 배열 입력
arr = input()

# 2진수로 변환
bin_num = ''
for i in arr:
    # 배열의 각 자리 i를 10진수로 표현
    a = int(i, 16)
    # 10진수로 표현한 a를 4자릿수로 채워서 2진수로 변환
    bin_num += bin(a)[2:].zfill(4)
    # bin_num += format(a, 'b')

# 7자리씩 끊어서 10진수로 변환
for num in range(0, len(bin_num), 7):
    temp = bin_num[num:num+7]
    ans = int(temp, 2)
    print(ans, end=' ')