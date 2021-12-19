import sys
sys.stdin = open('input.txt')

N = int(input())

ans = 0                              # 생성자 변수 0으로 초기화

for i in range(1, N+1):              # 1~ N만큼 반복
    ciphers = list(map(int, str(i))) # 숫자 i의 각 자릿수 리스트 생성
    total = i + sum(ciphers)         # 숫자 i와 i의 각 자릿수의 합을 total 변수로 설정 

    if total == N:                   # total 과 N이 일치하면
        ans = i                      # i를 생성자 ans에 할당
        break

print(ans)                           # 생성자 ans 출력 (없으면 0 출력)
