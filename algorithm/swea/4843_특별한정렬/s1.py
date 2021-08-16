import sys
sys.stdin = open('input.txt')

def selectionSort(a):

    # 0번째 인덱스부터 짝수 인덱스에 큰 값부터 내림차순으로 정렬
    for i in range(0, len(a)-1, 2):
        max = i
        for j in range(i+1, len(a)):
            if a[max] < a[j]:
                max = j
        a[i], a[max] = a[max], a[i]

    # 1번째 인덱스부터 홀수 인덱스에 작은 값부터 오름차순으로 정렬
    for i in range(1, len(a), 2):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    
    # 번갈아 정렬된 리스트 a를 반환
    return a



# 테스트 케이스 개수 T 입력
T = int(input())

# 테스트 케이스만큼 반복
for tc in range(1, T+1):
    
    # 정수의 개수 N 입력
    N = int(input())
    
    # 정렬한 N개의 정수를 arr 리스트에 저장
    arr = list(map(int, input().split()))

    # 결과 출력
    print('#{0}' .format (tc), end=' ')

    # selectionSort 함수에 arr 리스트를 넣는다
    selectionSort(arr)
    # 정렬된 arr 중 10개의 숫자만 출력
    for num in arr[0:10]:
        print(num, end=' ')
    print()