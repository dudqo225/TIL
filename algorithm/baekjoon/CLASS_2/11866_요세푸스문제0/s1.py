import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

numbers = list(range(1, N+1))

ans = []
while numbers:
    remain_1 = []
    remain_2 = []
    if len(numbers) == 1:
        ans.append(numbers[0])
        break
    elif len(numbers) == 2:
        if K % 2:
            ans.append(numbers[0])
            remain_1.append(numbers[1])
            numbers = remain_1
        else:
            ans.append(numbers[1])
            remain_1.append(numbers[0])
            numbers = remain_1
    else:
        deleted = False
        for i in range(len(numbers)):
            if i == K-1:
                deleted = True
                ans.append(numbers[i])
            if deleted == True and i != K-1:
                remain_2.append(numbers[i])
            elif deleted == False and i != K-1:
                remain_1.append(numbers[i])
        numbers = remain_2 + remain_1

print('<', end='')
for i in range(len(ans)-1):
    print('{}, '.format(ans[i]), end='')
print('{}>'.format(ans[-1]))