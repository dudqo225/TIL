arr = []

for _ in range(19):
    temp = list(map(int, input().split()))
    arr.append(temp)

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(19):
        if arr[i][y-1] == 0:
            arr[i][y-1] = 1
        else:
            arr[i][y-1] = 0

        if arr[x-1][i] == 0:
            arr[x-1][i] = 1
        else:
            arr[x-1][i] = 0

for a in arr:
    print(*a)