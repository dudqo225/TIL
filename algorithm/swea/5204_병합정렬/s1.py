import sys
sys.stdin = open('input.txt')

# 분할
def merge_sort(m):
    if len(m) == 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # append를 사용하면, 속도가 현저히 느려짐
    # for i in range(mid):
    #     left.append(m[i])
    # for i in range(mid, len(m)):
    #     right.append(m[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# 병합
def merge(left, right):
    global cnt

    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 cnt에 1 더한다.
    if left[-1] > right[-1]:
        cnt += 1


    i = 0
    left_i = 0
    right_i = 0
    left_len = len(left)
    right_len = len(right)

    result = [0] * (left_len + right_len)

    while left_i < left_len or right_i < right_len:
        if left_i < left_len and right_i < right_len:
            if left[left_i] <= right[right_i]:
                result[i] = left[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right[right_i]
                i += 1
                right_i += 1
        elif left_i < left_len:
            result[i] = left[left_i]
            i += 1
            left_i += 1
        elif right_i < right_len:
            result[i] = right[right_i]
            i += 1
            right_i += 1

    return result

# 테스트 케이스 T 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    ans = merge_sort(arr)

    print('#{} {} {}'.format(tc, ans[N//2], cnt))