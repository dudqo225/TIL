# 재귀 방식
def home(k, n):
    if k == 0:
        return n
    people = 0
    for j in range(1, n+1):
        people += home(k-1, j)
    return people


T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())

    print(home(k, n))


    '''
    # 1층 3호
    0층 1호, 2호, 3호

    # 2층 3호
    1층 1호: 0층 1호
    1층 2호: 0층 1호 0층 2호
    1층 3호: 0층 1호 0층 2호 0층 3호

    # 3층 3호
    2층 1호: 0층 1호
    2층 2호: 0층 1호, 0층 1호, 0층 2호
    2층 3호: 0층 1호, 0층 1호, 0층 2호, 0층 1호, 0층 2호, 0층 3호
    '''