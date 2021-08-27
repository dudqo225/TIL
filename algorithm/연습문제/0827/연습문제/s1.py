import sys
sys.stdin = open('input.txt')

# 전위 순회
def preorderT(T):
    if T:
        print(T, end=' ')
        preorderT(left[T])
        preorderT(right[T])

# 중위 순회
def inorderT(T):
    if T:
        inorderT(left[T])
        print(T, end=' ')
        inorderT(right[T])

# 후위 순회
def postorderT(T):
    if T:
        postorderT(left[T])
        postorderT(right[T])
        print(T, end=' ')

# 노드 개수 V
V = int(input())
# 간선 정보 입력
edge = list(map(int, input().split()))
# 간선의 수 = 노드의 수 -1
E = V - 1
    
# 왼쪽/오른쪽 자식 노드를 저장하는 리스트
left = [0] * (V+1)
right = [0] * (V+1)
    
# 간선 수만큼 반복
for i in range(E):
    # 부모, 자식 노드 분기
    p, c = edge[i*2], edge[i*2+1]
    # 부모 노드의 왼쪽 자식이 비어있으면 c를 저장
    if left[p] == 0:
        left[p] = c
    # 비어있지 않으면 오른쪽 자식에 c를 저장
    else:
        right[p] = c

print('전위 순회')
preorderT(1)
print('\n------------------------------------')

print('중위 순회')
inorderT(1)
print('\n------------------------------------')

print('후위 순회')
postorderT(1)
print('\n------------------------------------')