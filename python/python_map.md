# python | Map (Built-in Function)

#### `map(function, iterable)`

- 순회가능한 데이터 구조(iterable) 의 모든 요소에 function을 적용한 후 그 결과를 돌려줌
- return은 `map_object` 형태임



- **알고리즘 문제 풀이에서 자주 활용됨**
  - 코드 예시

```python
# 임의의 정수들을 입력받아 더한 값을 출력
user_input = sum(list(map(int, input().split())))

## 코드 실행 순서 ##
# 1. input() 으로 값을 입력받는다.
# 2. 입력받은 여려 값을 .split() 메서드로 나누어준다.
# 3. map() 함수로 각 값을 int로 형변환
# 4. 형변환한 값들을 list로 묶어준다.
# 5. list 내의 요소들을 sum() 함수로 모두 더해준다.
```



> map() 함수의 쓰임새를 잘 기억해두자. 👍

