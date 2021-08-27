# 부분집합 중 합이 10인 부분집합을 출력
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(data)
sel = [0] * N

def powerset(idx):
    # 아직 부분집합을 다 찾지 못한 경우
    if idx < N:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)
    # 전체 길이를 다 확인한 경우
    else:
        total = 0
        for i in range(N):
            if sel[i]:
                total += data[i]

        if total == 10:
            for i in range(N):
                if sel[i]:
                    print(data[i], end=' ')
            print()
        return


powerset(0)