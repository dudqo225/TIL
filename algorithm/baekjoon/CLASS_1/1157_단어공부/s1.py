import sys
sys.stdin = open('input.txt')

'''
풀이.
1. 입력받는 알파벳 단어를 전부 대문자로 바꾼다.
2. 단어에서 중복을 제거한 알파벳 리스트를 생성한다.
3. 각 알파벳이 몇번 나타났는지 .count()를 활용하여 세어준다.
4. cnt 리스트 내의 최대값이 여러개일 경우 ?를 출력한다.
5. 아닐경우, cnt 리스트의 초대값의 인덱스를 찾고 word_list의 해당 인덱스 값을 출력한다.
'''
words = input().upper()
word_list = list(set(words))

cnt = []

for i in word_list:
    temp = words.count(i)
    cnt.append(temp)

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    max_idx = cnt.index(max(cnt))
    print(word_list[max_idx])