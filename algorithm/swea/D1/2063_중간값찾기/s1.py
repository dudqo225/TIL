import sys
sys.stdin = open('input.txt')

# N 입력
N = int(input())

# N 개의 점수를 num_list 로 입력
num_list = list(map(int, input().split()))

# 중앙값 인덱스 구하기
mid_idx = N // 2

# 숫자 리스트를 정렬
num_list.sort()

# 결과 출력
print(num_list[mid_idx])
