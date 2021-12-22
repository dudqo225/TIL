# Algorithm | 백준 1018.체스판 다시 칠하기 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 1018.체스판 다시 칠하기 링크](https://www.acmicpc.net/problem/1018)

</br>

#### 문제

지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

</br>

#### 코드

```python
N, M = map(int, input().split())

chess = [[i for i in input()] for _ in range(N)]

results = []

for i in range(N-7):
    for j in range(M-7):
        w_cnt = 0
        b_cnt = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if chess[x][y] != 'W':
                        w_cnt += 1
                    if chess[x][y] != 'B':
                        b_cnt += 1
                else:
                    if chess[x][y] != 'B':
                        w_cnt += 1
                    if chess[x][y] != 'W':
                        b_cnt += 1
        results.append(min(w_cnt, b_cnt))

ans = min(results)

print(ans)
```

</br>

#### 틀린 코드

```python
# 첫번째
def check(arr):

    cnt = 0
    if arr[0][0] == 'B':
        for i in range(N):
            for j in range(M//2):
                if arr[i][2*j] != 'B':
                    cnt += 1
                if arr[i][2*j+1] != 'W':
                    cnt += 1
    else:
        for i in range(N):
            for j in range(M//2):
                if arr[i][2*j] != 'W':
                    cnt += 1
                if arr[i][2*j+1] != 'B':
                    cnt += 1

    return cnt


# 두번째
def check(arr):

    cnt = 0

    i, j = 0, 0
    current = arr[0][0]

    while i < N:

        if current != arr[i][j]:
            cnt += 1
        if current == 'W':
            current = 'B'
        else:
            current = 'W'

        print(i, j, current)
        if j == M-1:
            i += 1
            j = 0
            continue
        j += 1

    return cnt
```

- 첫번째 코드는 for문을, 두번째 while문을 활용하여 문제를 풀었으나 해결하지 못하였다. 



#### 풀이

```python
4중 for문을 활용하여 문제를 해결하였다.
입력받은 N, M 중에서 8x8 크기의 체스판에 대해서만 색깔 확인을 해야 하므로, 처음 2중 for문에서는 N-7, M-7로 i와 j 범위를 설정하고 다음 2중 for문에서 i~i+8, j~j+8로 범위를 설정한다.

흰색, 검은색 여부 확인은 브루트 포스 개념을 사용하여 가능한 전체 경우를 확인하고 최적의 해를 구한다.

x, y 인덱스의 합이 짝수일 경우 / 홀수일 경우에 따라 색깔이 교차적으로 반복되기 때문에 (x+y) % 2 == 0조건을 통해 확인한다.

각각의 w_cnt, b_cnt 중 최소값을 results 리스트에 추가하고 이 리스트에서 최소값을 결과 ans에 할당하여 출력한다.
```



#### 참고

https://bambbang00.tistory.com/43

https://god-gil.tistory.com/62

위 2개 블로그 글 모두, 4중 for문을 반복하여 문제를 해결하였다.



✨ 알고리즘 공부 5개월째, 여전히 i, j 등의 Index 컨트롤이 쉽지 않다. 그리고 좀더 간단하게 생각해도 되는 문제인데, 너무 꼬으고 꼬아서 생각하다보니 문제가 더 어렵게 느껴지는 것 같다. 인덱스를 자유자재로 조작하는 부분을 더 연습하자! 2021.12.22
