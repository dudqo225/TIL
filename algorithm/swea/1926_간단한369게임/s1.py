N = int(input())

for i in range(1, N+1):
    cnt = 0
    for j in range(len(str(i))):
        if str(i)[j] in ['3', '6', '9']:
            cnt += 1
    if cnt == 0:
        print(i, end=' ')
    else:
        print('-' * cnt, end=' ')