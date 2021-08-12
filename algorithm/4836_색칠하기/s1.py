import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 T를 받아오기
T = int(input())

# 테스트 케이스 T만큼 반복
for tc in range(1, T+1):

    # 색칠할 영역 개수 N 입력
    N = int(input())

    # 빨간색, 파란색 박스의 인덱스를 저장할 리스트 생성
    red_box = []
    blue_box = []

    # 색칠할 영역 개수만큼 반복
    for _ in range(N):
        # 왼쪽 위 모서리 인덱스, 오른쪽 아래 모서리 인덱스, 색상 정보 입력
        r1, c1, r2, c2, color = map(int, input().split())

        # 빨간색일 때
        if color == 1:
            # 왼쪽 위 모서리부터 오른쪽 아래 모서리까지 순회
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    # 행렬 인덱스를 red_box 리스트에 추가
                    red_box.append((i,j))
        
        # 파란색일 때
        if color == 2:
            # 왼쪽 위 모서리부터 오른쪽 아래 모서리까지 순회
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    # 행렬 인덱스를 blue_box 리스트에 추가
                    blue_box.append((i,j))

    # 길이가 더 큰 박스색 찾기
    if len(red_box) > len(blue_box):
        max_len = len(red_box)
        l_box, s_box = red_box, blue_box
    else:
        max_len = len(blue_box)
        l_box, s_box = blue_box, red_box

    # 보라색이 된 칸 수 구하기
    cnt = 0
    for i in range(max_len):
        if l_box[i] in s_box:
            cnt += 1

    # 결과 출력
    print('#{0} {1}'.format (tc, cnt))


