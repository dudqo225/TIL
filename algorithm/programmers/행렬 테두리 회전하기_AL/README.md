# Programmers | 행렬 테두리 회전하기 (AL)

> 본 문제의 저작권은 프로그래머스에 있습니다.
>
> [행렬 테두리 회전하기 링크](https://programmers.co.kr/learn/courses/30/lessons/77485)

</br>

#### 문제 설명

rows x columns 크기인 행렬이 있습니다. 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다. 이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다. 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 다음과 같습니다.

- x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.

다음은 6 x 6 크기 행렬의 예시입니다.

![grid_example.png](images/grid_example.png)

이 행렬에 (2, 2, 5, 4) 회전을 적용하면, 아래 그림과 같이 2행 2열부터 5행 4열까지 영역의 테두리가 시계방향으로 회전합니다. 이때, 중앙의 15와 21이 있는 영역은 회전하지 않는 것을 주의하세요.

![rotation_example.png](images/rotation_example.png)

행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때, 각 회전들을 배열에 적용한 뒤, 그 회전에 의해 위치가 바뀐 숫자들 중 **가장 작은 숫자들을 순서대로 배열에 담아** return 하도록 solution 함수를 완성해주세요.

</br>

#### 제한사항

- rows는 2 이상 100 이하인 자연수입니다.
- columns는 2 이상 100 이하인 자연수입니다.
- 처음에 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀있습니다.
  - 즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
- queries의 행의 개수(회전의 개수)는 1 이상 10,000 이하입니다.
- queries의 각 행은 4개의 정수 [x1, y1, x2, y2]입니다.
  - x1 행 y1 열부터 x2 행 y2 열까지 영역의 테두리를 시계방향으로 회전한다는 뜻입니다.
  - 1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns입니다.
  - 모든 회전은 순서대로 이루어집니다.
  - 예를 들어, 두 번째 회전에 대한 답은 첫 번째 회전을 실행한 다음, 그 상태에서 두 번째 회전을 실행했을 때 이동한 숫자 중 최솟값을 구하면 됩니다.

</br>

#### 코드

```python
def solution(rows, columns, queries):
    answer = []

    mat = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            mat[i][j] = ((i) * columns) + (j+1)

    def rotate(x_1, y_1, x_2, y_2, start_val):
        min_val = 9876543210
        for a in range(y_1+1, y_2+1):
            min_val = min(min_val, start_val)
            mat[x_1][a], start_val = start_val, mat[x_1][a]

        for b in range(x_1+1, x_2+1):
            min_val = min(min_val, start_val)
            mat[b][y_2], start_val = start_val, mat[b][y_2]

        for c in range(y_2-1, y_1-1, -1):
            min_val = min(min_val, start_val)
            mat[x_2][c], start_val = start_val, mat[x_2][c]

        for d in range(x_2-1, x_1-1, -1):
            min_val = min(min_val, start_val)
            mat[d][y_1], start_val = start_val, mat[d][y_1]

        return min_val

    for query in queries:
        x1, y1, x2, y2 = query
        before = mat[x1-1][y1-1]
        answer.append(rotate(x1-1, y1-1, x2-1, y2-1, before))

    return answer
```

</br>

#### 풀이

- **인덱스**를 조정하여 문제 풀이 진행
- `rotate()` 함수를 수행할 때, 반복문을 **4번** 돌린다.
  1. `→`. 오른쪽 방향
  2. `↓`. 아래 방향
  3. `←`. 왼쪽 방향
  4. `↑`. 위 방향
  5. 반복문을 수행할 때, 움직이는 칸 중에서 **가장 작은 수**를 `min_val` 변수에 담는다.