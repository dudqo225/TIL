import sys
sys.stdin = open('input.txt')

bitpattern  = [
    '001101', # 0
    '010011', # 1
    '111011', # 2
    '110001', # 3
    '100011', # 4
    '110111', # 5
    '001011', # 6
    '111101', # 7
    '011001', # 8
    '101111', # 9
]

arr = input()

bin_num = ''
for i in arr:
    a = int(i, 16)
    bin_num += str(bin(a)[2:].zfill(4))

result = []

i = 0
while i < len(bin_num) - 5:
    if bin_num[i:i+6] in bitpattern:
        result.append(str(bitpattern.index(bin_num[i:i+6])))
        i += 6
    else:
        i += 1

print(', '.join(result))