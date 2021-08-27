import sys
sys.stdin = open('input.txt')

# bfs 함수
def bfs(v):
    global G
    # 첫번째 v는 시작노드. Q 리스트에 저장하고 방문했다는 의미로 visited[v] = 1
    Q = [v]
    visited[v] = 1

    # Q가 비어질 때까지 반복
    while Q:
        # Q의 첫번째 값을 v로 한다.
        v = Q.pop(0)

        # v가 도착노드와 같다면, visited[v]에서 1뺀 값을 리턴 (거리를 계산하기 위해서)
        if v == G:
            return visited[v] - 1

        # 인접 노드를 찾기 위해 반복문 수행
        for w in range(1, V+1):
            # 인접노드이면서 아직 방문하지 않았다면
            if graph[v][w] == 1 and visited[w] == 0:
                # Q에 추가하고, v의 이동거리 + 1 해준다.
                Q.append(w)
                visited[w] = visited[v] + 1
    
    # 탐색을 전부하였으나 연결되지 않았다면 0을 리턴
    return 0

T = int(input())
for tc in range(1, T+1):
    # 노드 V, 간선 E 입력
    V, E = map(int, input().split())
    # 간선의 노드 번호 리스트 생성
    graph_list = [list(map(int, input().split())) for _ in range(E)]
    # 출발노드 S, 도착노드 G 입력
    S, G = map(int, input().split())

    # 인덱스를 편리하게 하기 위해서 0~V 까지의 graph, visited 생성
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    # 간선의 수만큼 반복
    for i in range(E):
        # 간선의 양쪽 노드 번호를 각각 start, end에 저장
        start = graph_list[i][0]
        end = graph_list[i][1]
    
        # 무방향 그래프
        graph[start][end] = 1
        graph[end][start] = 1
    
    # 결과 출력
    print('#{} {}'.format(tc, bfs(S)))