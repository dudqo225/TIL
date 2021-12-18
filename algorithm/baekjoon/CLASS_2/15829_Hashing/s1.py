import sys
sys.stdin = open('input.txt')

hash_alpha = [0, 'a', 'b', 'c', 'd', 'e', 'f',
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']

r = 31
M = 1234567891

L = int(input())
words = input()

total = 0

for idx, word in enumerate(words):
    val = hash_alpha.index(word)
    total += val * r ** idx

H = total % M

print(H)