# Programmers | 정렬 - K번째수

> 본 문제의 저작권은 프로그래머스에 있습니다.



#### 문제 설명

```
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
```



#### 제한사항

- array의 길이는 1 이상 100 이하입니다.
- array의 각 원소는 1 이상 100 이하입니다.
- commands의 길이는 1 이상 50 이하입니다.
- commands의 각 원소는 길이가 3입니다.



#### 입출력 예

| array                 | commands                          | return    |
| --------------------- | --------------------------------- | --------- |
| [1, 5, 2, 6, 3, 7, 4] | [[2, 5, 3], [4, 4, 1], [1, 7, 3]] | [5, 6, 3] |



#### 코드

```python
def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        temp = array[commands[i][0]-1:commands[i][1]]
        temp.sort()
        answer.append(temp[commands[i][2]-1])
    
    return answer
```



#### 풀이

`commands` 리스트 길이만큼 순회하면서 주어진 조건에 맞는 숫자를 찾아낸다. 정렬 문제이기 때문에 여러가지 정렬 알고리즘을 사용할까 생각해보았지만 일반적으로 코테에서는 `.sort()` 와 같은 함수 사용이 가능한 것으로 알고 있기 때문에 간단하게 정렬하여 결과값을 구하였다. `for` 문 중간에 Index를 정하는 부분을 주의하면 쉽게 문제를 풀 수 있다.



##### 다른 사람의 풀이

```python
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```

- 람다식으로 단 2줄에 풀어버리네... 🤣

