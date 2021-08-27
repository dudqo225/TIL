arr = [1, 2, 3]

N = len(arr)

sel = [0] * N

def powerset(idx):
    if idx == N:
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return

    # sel 배열의 index 자리를 1로 바꾼다 => 해당 원소를 뽑았다!
    sel[idx] = 1
    powerset(idx+1)

    # sel 배열의 index 자리를 0으로 바꾼다 => 해당 원소를 뽑지 않는 경우!
    sel[idx] = 0
    powerset(idx+1)


powerset(0)