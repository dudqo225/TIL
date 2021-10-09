import sys
sys.stdin = open('input.txt')

# 입력받은 문자열을 10진수로 변환
def change_number(num, notation):
    # 임시 변수 tmp를 0으로 초기화
    tmp = 0
    # enumerate로, 인덱스와 값을 순회
    # 순회할 대상은 num을 뒤집어서 반복한다.
    # 왜? 예를 들어, 2진수 '1010' 이면 '0101'로 반복할 때 2**0, 2**1, 2**2, 2**3 순으로 계산이 가능하기 때문
    for idx, val in enumerate(list(map(int, num))[::-1]):
        tmp += (notation**idx) * val

    # 10진수로 변환한 수를 반환
    return tmp

# 한 자리의 값만 교체를 하면서 송금액이 될 가능성이 있는 숫자를 확인
def check(num, notation):
    # num을 10진수로 변경
    change_num = change_number(num, notation)

    # enumerate로 인덱스, 값을 같이 반복 순회
    for idx, val in enumerate(list(map(int, num))[::-1]):
        # 진수에 따른 범위 설정 (2진수면 0, 1 / 3진수면 0, 1, 2)
        for j in range(notation):
            # 자릿수가 j와 동일하다면 continue
            if val == j: continue
            # 동일하지 않으면 아래 수식 계산
            # tmp 변수에 할당 > 10진수로 변경한 수에서 기존 val에 해당하는 수를 빼고, j로 새롭게 비트전환한 수를 더한다.
            tmp = change_num - val * (notation**idx) + j * (notation**idx)

            # tmp 수가 candidate 안에 없으면, 추가
            if tmp not in candidate:
                candidate.append(tmp)
            # 이미 있으면 tmp를 반환
            else:
                return tmp

T = int(input())
for tc in range(1, T+1):
    bina_num = input()
    tri_num = input()

    candidate = []
    # 2진수의 숫자를 먼저 확인
    check(bina_num, 2)

    # 그 후 3진수 숫자를 확인하면, 중복되는 숫자가 결과로 나온다.
    # 중복되는 숫자다 >> 2진수, 3진수 모두 송금액으로 가능한 숫자이기 때문에 그 숫자가 정답
    print('#{} {}'.format(tc, check(tri_num, 3)))