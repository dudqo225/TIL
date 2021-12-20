import sys
sys.stdin = open('input.txt')

end = '666'
N = int(input())

i = 0

for j in range(N):
    i = j

ans = str(i) + end

print(ans)