import sys
sys.stdin = open('input.txt')

def dfs(result, person):
    global mat, visited, max_res

    # 가지치기
    if result <= max_res:
        return

    # N명에게 일분배를 다 했을 때의 최대확률과 result 비교
    if person == N:
        if max_res <= result:
            max_res = result
        return
    
    # dfs 구조
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(result*mat[person][i]*0.01, person+1) # 재귀
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_res = 0

    dfs(1, 0)

    # 확률 표기법 변경
    res = format(max_res*100, ".6f")

    # 결과 출력
    print('#{} {}'.format(tc, res))