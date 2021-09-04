# Algorithm | Stack2

### 목차

> - 계산기
> - 백트래킹
> - 부분집합, 순열
> - 분할정복

</br></br>

### 1. 계산기

- 중위표기법 (infix notation)
  - 연산자를 피연산자 가운데에 표기하는 방법
  - `A+B`
- 후위표기법 (postfix notation)
  - 연산자를 피연산자 뒤에 표기하는 방법
  - `AB+`

- 중위표기법을 후위표기법으로 바꾸고 계산하는 알고리즘
  - `swea` 문제 풀이 참고
    - [swea_1223_계산기2](https://github.com/dudqo225/TIL/tree/master/algorithm/swea/1223_%EA%B3%84%EC%82%B0%EA%B8%B02)
    - [swea_1224_계산기3](https://github.com/dudqo225/TIL/tree/master/algorithm/swea/1224_%EA%B3%84%EC%82%B0%EA%B8%B03)

<br>

### 2. 백트래킹

- 백트래킹(Backtracking) 기법은 해를 찾는 도중에 막히면, 되돌아가서 다시 해를 찾아가는 기법
- 최적화(optimization) 문제와 결정(decision) 문제를 해결할 수 있음
- 결정(decision) 문제
  - 문제의 조건을 만족하는 해가 존재하는지 여부를 yes / no 로 답하는 문제
    - 미로 찾기
    - n-Queen 문제
    - Map coloring
    - 부분집합의 합(Subset Sum) 문제
    - etc.

- 백트래킹 vs DFS 차이
  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 그 경로를 따라가지 않음으로써 시도 횟수를 줄임 (**Prunning 가지치기**)
  - DFS는 모든 경로를 추적. 백트래킹은 불필요한 경로를 조기에 차단
  - N! 가지의 경우의 수를 가진 문제에 대해서는 DFS 로 처리가 불가능
  - 백트래킹 알고리즘을 적용하면 경우의 수가 줄어들지만, 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 필요로 하기때문에 처리 불가능

<br>

### 3. 부분집합, 순열

#### 부분집합

- 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합을 powerset 이라고 한다.
- 구하고자 하는 집합의 원소 개수가 `n` 일때, 부분집합의 개수는 `2ⁿ` 개 이다.

```python
# 각 원소가 부분집합에 포함되었는지 loop 를 이용해서 확인하고 부분집합을 생성하는 방법
bit = [0, 0, 0, 0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
```

```python
# powerset을 구하는 백트래킹 알고리즘
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    
    if k == input:
        process_solution(a, k) # 답이면 원하는 작업을 한다
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
            
def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
```

<br>

#### 순열

```python
# {1, 2, 3} 을 포함하는 모든 순열을 생성하는 함수. Loop 활용
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
```

```python
# 백트래킹을 이용해서 순열 구하기
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    
    if k == input:
        for i in range(1, k+1):
            print(a[i], end=' ')
        print()
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
            
def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX
    
    for i in range(1, k):
        in_perm[a[i]] = True
    
    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidtaes += 1
    return ncandidates
```

<br>

### 4. 분할정복

#### 유래

- 1805년 12월 2일 아우스터리츠 전투에서 나폴레옹이 사용한 전략
- 연합군 중앙부로 쳐들어가서 연합군을 둘로 나누고, 둘로 나뉜 연합군을 한 부분씩 격파

#### 설계전략

- **분할(Divide)** : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- **정복(Conquer)** : 나눈 작은 문제를 각각 해결한다.
- **통합(Combine)** : 해결된 해답을 모은다.

```python
# 거듭 제곱(Exponentiation) 예시
def Power(base, exponent):
    if exponent == 0 or base == 0:
        return 1
    
    if exponent % 2 == 0: # 짝수일 때
        newBase = Power(base, exponent/2)
        return newBase * newBase
   	else: # 홀수일 때
        newBase = Power(base, (exponent-1)/2)
        return (newBase * newBase) * base
```

<br>

#### 퀵 정렬

- 주어진 배열을 2개로 분할하고, 각각을 정렬한다.
- 퀵 정렬 vs 합병 정렬
  - 합병 정렬은 그냥 두 부분으로 나눈다.
  - 퀵 정렬은 기준 아이템(pivot item)을 중심으로 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.
  - 각 부분 정렬이 끝난 후에 합병 정렬은 `합병` 이라는 후처리 작업이 필요하고, 퀵 정렬은 필요로 하지 않음

```python
# 퀵정렬 알고리즘
def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
        
def partition(a, begin, end):
    pivot = (begint + end) // 2
    L = begin
    R = end
    while L < R:
        while(L<R and a[L]< a[pivot]): L += 1
        while(L<R and a[R]> a[pivot]): R -= 1
        if L < R:
            if L == pivot: pivot = R
            a[L], a[R] = a[R], a[L]
   	a[pivot], a[R] = a[R], a[pivot]
    return R
```

- 시간 복잡도
  - 최악의 경우 : `O(n²)` → 합병정렬에 비해 좋지 못하다.
  - 평균 복잡도 : `O(nlogn)` → 평균적으로는 가장 빠르다.

<br>

> 2021.09.04 부분집합과 순열 파트 & 퀵 정렬 알고리즘은 잘 이해되지 않는다...😂