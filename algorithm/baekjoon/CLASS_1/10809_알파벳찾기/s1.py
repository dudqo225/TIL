import sys
sys.stdin = open('input.txt')

words = input()

idx_list = [-1] * 26


for i in range(len(words)):
    # words 각 알파벳을 아스키코드 숫자로 변환 후 97을 빼주면, 1~26 인덱스를 얻을 수 있음
    x = ord(words[i])-97

    if idx_list[x] == -1:
        idx_list[x] = i

for idx in idx_list:
    print(idx, end=' ')