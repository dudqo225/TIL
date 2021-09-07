import sys
sys.stdin = open('input.txt')

T = 1
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            temp1 = arr[i][j]
            temp2 = arr[j][i]
            if temp1 != 0:
                row[temp1] = 1
            if temp2 != 0:
                col[temp2] = 1

            # if arr[i][j] == 0:
            #     for x in range(1, 10):
            #         if x not in num:
            #             arr[i][j] = x
            #
            # if arr[j][i] == 0:
            #     for x in range(1, 10):
            #         if x not in num:
            #             arr[j][i] = x

            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        temp3 = arr[a][b]
                        if temp3 != 0:
                            square[temp3] = 1


    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=' ')
        print()