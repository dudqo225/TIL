import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 T 입력
T = int(input())
for tc in range(1, T+1):
    # 화덕 크기 N, 피자 수 M 입력
    N, M = map(int, input().split())
    # M개 피자의 치즈 양을 리스트로 입력
    cheese = list(map(int, input().split()))

    # 피자의 번호와 치즈 양을 저장하기 위한 pizza 리스트 생성
    pizza = []
    # enumerate() 함수로 피자의 인덱스와 치즈 양을 pizza 리스트에 추가
    for idx, val in enumerate(cheese):
        pizza.append([idx, val])

    # 화덕에 넣는 피자의 정보를 저장하기 위해 Q 생성
    Q = []
    # N만큼 화덕에 피자를 넣어준다.
    for _ in range(N):
        Q.append(pizza.pop(0))

    # 화덕에 피자가 한개 남을때까지 반복
    while len(Q) != 1:
        # 첫번째 피자의 치즈 양을 // 2 해준다.
        Q[0][1] //= 2
        # 치즈의 양이 0일 경우
        if Q[0][1] == 0:
            # 피자를 빼준다.
            Q.pop(0)
            # 화덕 밖의 피자가 남아있는 경우, 화덕에 피자를 넣어준다.
            if pizza:
                Q.append(pizza.pop(0))
        # 치즈의 양이 0이 아닐 경우
        else:
            # 화덕을 한번 돌려준다.
            Q.append(Q.pop(0))

    # 인덱스 +1 해줘야 피자 번호가 나온다.
    ans = Q.pop(0)[0] + 1

    # 결과 출력
    print('#{} {}'.format(tc, ans))