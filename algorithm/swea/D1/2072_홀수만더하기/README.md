# Algorithm | sum_odd

### 문제

> #### 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라
>
> ##### [제약사항]
>
> 각 수는 0 이상 10000 이하의 정수이다.



### 입출력

#### 입력 예시

```
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1
```

#### 출력 예시

```
#1 200
#2 208
#3 121
```



### 풀이

```python
# 테스트 케이스 개수 T
T = int(input())

# 테스트 케이스 개수 T만큼 반복
for test_case in range(T):
    # 10개의 정수를 입력받아 map() 함수로 int 형변환. 형변환한 값들을 list로 저장
    user_input = list(map(int, input().split(' ')))
    # 총합 total 변수 초기화
    total = 0
    # 10개의 숫자를 반복
    for num in user_input:
        # 숫자가 홀수라면, total에 그 숫자를 더해준다.
        if num % 2 == 1:
            total += num
    # 결과 출력 형태 지정 f-string
    print(f'#{i+1} {total}')
```



### 정리

- 위 코드는 `jupyter notebook` 이나 `VSC`에서 돌려보면 제대로 나온다.
- 하지만, SWEA 에서 테스트 케이스를 돌리면 아래와 같은 에러 메시지가 출력된다.

```
Memory error occured, (e.g. segmentation error, memory limit Exceed, stack overflow,... etc)
```

- 메모리 초과라... 저렇게 돌리면 스택 메모리가 1MB를 넘는건가?? 메모리 개념을 알아야 뭘 고치든말든하지..
- 알고리즘 쌩기초 문제인데도 어렵다 🤣 (21.07.30)



> #### 해당 알고리즘 문제는 [SW Expert Academy](https://swexpertacademy.com/main/main.do) 2072. 홀수만 더하기 `D1` 문제이다.



