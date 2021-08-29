import sys
sys.stdin = open('input.txt')

# 가로 x 세로 길이 찾기
def findWH(i, j):
    # 가로 길이 찾기
    width = 1
    dx = j
    while True:
        dx += 1
        # 범위를 넘어가면 반복을 종료
        if dx >= n:
            break
        # 해당 인덱스에 값이 있으면 가로 길이를 1 늘려준다.
        if mat[i][dx]:
            width += 1
        # 해당 인덱스에 값이 없으면 반복 종료
        else:
            break
    # 세로 길이 찾기
    height = 1
    dy = i
    while True:
        dy += 1
        # 범위를 넘어가면 반복을 종료
        if dy >= n:
            break
        # 해당 인덱스에 값이 있으면 세로 길이를 1 늘려준다.
        if mat[dy][j]:
            height += 1
        # 해당 인덱스에 값이 없으면 반복 종료
        else:
            break
    
    # 가로, 세로 길이를 리턴
    return width, height

# 이미 탐색한 부분행렬 값 0으로 바꾸기
def changeZero(s_i, s_j, e_i, e_j):
    for i in range(s_i, e_i):
        for j in range(s_j, e_j):
            mat[i][j] = 0

# 테스트 케이스 개수 T 입력
T = int(input())
for tc in range(1, T+1):
    # 행렬 크기 n 입력
    n = int(input())

    # 행렬 입력
    mat = [list(map(int, input().split())) for _ in range(n)]

    # 부분행렬 값 저장하기 위한 빈 리스트 생성
    ans_list = []
    for i in range(n):
        for j in range(n):
            # 해당 위치가 비어있지 않다면, 가로x세로 크기를 탐색
            if mat[i][j]:
                # findWH 함수로 가로, 세로 길이를 확인
                w, h = findWH(i, j)
                # 부분행렬을 0으로 바꾸어서 중복 탐색을 방지
                changeZero(i, j, i+h, j+w)
                # ans_list에 행렬의 높이, 길이, 크기를 저장
                ans_list.append([h, w, h*w])
    
    # 크기, 높이 순으로 ans_list를 정렬
    ans = sorted(ans_list, key=lambda x: (x[2], x[0]))
    
    # 결과 출력
    print('#{} {}'.format(tc, len(ans)), end=' ')
    for h, w, hw in ans:
        print(h, w, end=' ')
    print()
