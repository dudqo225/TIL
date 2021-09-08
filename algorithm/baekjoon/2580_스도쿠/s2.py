import sys
sys.stdin = open('input.txt')

def sudoku(M):

    for i in range(9):
        r_stack = []
        row = [0] * 10
        c_stack = []
        col = [0] * 10
        # 가로 검사
        for j in range(9):
            if M[i][j] == 0:
                r_stack.append([i, j])
            else:
                row[M[i][j]] = 1
        for x in range(1, 10):
            if row[x] == 0:
                idx = r_stack.pop()
                M[idx[0]][idx[1]] = x

        # 세로 검사
        for


T = 1
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]