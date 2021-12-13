import sys
sys.stdin = open('input.txt')

# 학점 리스트
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 총점 리스트 생성
    total_score = []
    for _ in range(N):
        score = list(map(int, input().split()))
        total_score.append(score[0]*0.35 + score[1]*0.45 + score[2]*0.2)

    # K번째 학생의 점수와 인덱스 변수 생성
    target_score = total_score[K-1]
    target_score_idx = 0

    # 내림차순으로 정렬된 총점 리스트 생성
    student_grade_score = sorted(total_score, reverse=True)

    # K번째 학생의 등수 확인
    for i in range(N):
        # 정렬된 총점 리스트를 순회하면서 K번째 학생의 점수와 같으면
        if student_grade_score[i] == target_score:
            target_score_idx = i // (N // 10)

    ans = grade[target_score_idx]
    print('#{} {}'.format(tc, ans))