import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, numbers = list(input().split())

    # N int로 형 변환
    N = int(N)

    # ans에 numbers 복사
    ans = numbers[:]

    # 인덱스를 조정하며 반복문 돌리기
    i = 0
    while i < len(ans):                            # i가 ans 길이를 넘어서면 반복문 종료
        if i < len(ans)-1 and ans[i] == ans[i+1]:  # ans의 i번째 값과 그 다음 값이 일치하면,
            ans = ans[:i] + ans[i+2:]              # 일치하는 쌍을 제외하고 ans를 재할당
            i = 0                                  # i는 0으로 초기화
        else:                                      # ans의 i번째 값과 그 다음 값이 일치하지 않으면
            i += 1                                 # i는 1 증가
    
    # 결과 출력
    print('#{} {}'.format(tc, ans))

