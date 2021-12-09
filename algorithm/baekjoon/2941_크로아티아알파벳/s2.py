import sys
sys.stdin = open('input.txt')

'''
s1 파일에서는 인덱스 조정을 통한 ans를 구하려고 시도하였으나, 계속해서 IndexError가 발생하였다.
구글링을 통해, .replace() 메서드로 답을 구하는 방법을 알게되었다.
각각의 크로아티아 알파벳을 전혀 관련없는 문자열(+, * 등)로 바꾼 후
alpha 리스트의 길이를 구한다.
'''

alpha = input()

cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for cro in cro_alpha:
    alpha = alpha.replace(cro, '+')

print(len(alpha))