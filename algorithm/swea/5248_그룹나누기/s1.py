import sys

sys.stdin = open('input.txt')

def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    parent[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    # make-set
    parent = [i for i in range(N + 1)]

    # 신청서별로 union
    for i in range(M):
        union(arr[2 * i], arr[2 * i + 1])

    # 부모노드를 중복없이 저장하기 위해 빈 set 생성
    ans = set()

    # 1~ N까지 순회하면서 부모노드의 값을 ans에 저장
    for i in range(1, N+1):
        ans.add(find_set(i))

    # ans의 길이 = 생성된 조의 개수
    print('#{} {}'.format(tc, len(ans)))
