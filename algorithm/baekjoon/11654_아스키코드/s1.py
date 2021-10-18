import sys
sys.stdin = open('input.txt')

T = 6
for tc in range(1, T+1):
    word = input()

    print(ord(word))