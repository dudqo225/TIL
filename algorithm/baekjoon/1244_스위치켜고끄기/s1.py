import sys
sys.stdin = open('input.txt')

# 스위치 개수 입력
S = int(input())

# 스위치 리스트 입력
s_list = list(map(int, input().split()))

# 학생수 입력
students_num = int(input())

# 학생수만큼 반복
for _ in range(students_num):
    # 성별과 학생이 받은 수 입력
    gender, num = map(int, input().split())
    
    # gender 남학생 1일 경우
    if gender == 1:
        # 학생이 받은 수의 배수를 다 바꿔야한다.
        for i in range(num-1, S, num):
            # 0이면 1로
            if s_list[i] == 0:
                s_list[i] = 1
            # 1이면 0으로
            else:
                s_list[i] = 0
    
    # gender 여학생 2일 경우
    else:
        # 받은 수에 위치한 스위치를 0 ↔ 1 변경
        if s_list[num-1] == 0:
            s_list[num-1] = 1
        else:
            s_list[num-1] = 0
    
        # i는 학생이 받은 스위치 왼쪽, j는 스위치 오른쪽
        i = num-2
        j = num
        # i와 j가 0~S 인덱스 범위내에 있을동안 반복
        while i >= 0 and j < S:
            # i번째 스위치와 j번째 스위치가 동일할 경우
            if s_list[i] == s_list[j]:
                # 0일 경우 1로 바꾸고
                if s_list[i] == 0:
                    s_list[i], s_list[j] = 1, 1
                # 1일 경우 0으로 바꿔준다
                else:
                    s_list[i], s_list[j] = 0, 0
            # 동일하지 않으면 바로 while문 종료
            else:
                break
            # i는 왼쪽으로 한칸 더, j는 오른쪽으로 한칸 더
            i -= 1
            j += 1

# 결과 출력. 한 줄에 20개씩 출력한다.
for s in range(0, S, 20):
    print(*s_list[s:s+20])