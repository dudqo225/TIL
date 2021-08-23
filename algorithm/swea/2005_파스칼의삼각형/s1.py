import sys
sys.stdin = open('input.txt')

'''
문제
크기가 N인 파스칼의 삼각형을 만들어야 한다.
파스칼 삼각형이란?
1) 첫 번째 줄은 항상 숫자 1
2) 두 번째 줄부터 각 숫자들은 자신의 왼쪽 위, 오른쪽 위의 숫자의 합으로 구성된다.

제약사항
파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다.

입력
첫 줄에 테스트 케이스 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.

출력
각 줄은 '#t'로 시작. 다음 줄부터 파스칼의 삼각형을 출력한다.
삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.
'''

# 테스트케이스 개수 T 입력
T = int(input())
# T만큼 테스트 반복
for tc in range(1, T+1):
    # 파스칼 삼각형의 크기 N 입력
    N = int(input())

    # 파스칼 삼각형 출력을 위한 NxN 리스트 생성
    arr = [[0] * N for _ in range(N)]

    # i는 0부터 N-1까지
    for i in range(N):
        # j는 0부터 i까지
        for j in range(i+1):
            # 각 열의 좌우 끝은 1로 고정
            if j == 0 or j == i:
                arr[i][j] = 1
            # 그외에는, 왼쪽 위와 오른쪽 위의 값을 더한 값을 할당
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    # 결과 출력
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                print(arr[i][j], end=' ')
        print()
