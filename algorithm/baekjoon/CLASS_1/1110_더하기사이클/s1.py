import sys
sys.stdin = open('input.txt')

a = input()

if int(a) < 10:
    a = '0' + a

cnt = 0
new_a = a

while True:
    new_a = new_a[-1] + str(int(new_a[0]) + int(new_a[1]))[-1]
    cnt += 1

    if new_a == a:
        break

print(cnt)