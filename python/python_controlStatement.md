## python_controlStatement

- 제어문은 순서도(flow chart)로 표현이 가능



### 1. 조건문 (Conditional Statement)

- if ~ elif ~ else 문



### 2. 반복문 (Loop Statement)

- while

  - 종료 조건에 해당하는 코드를 통해 반복문을 종료 시켜야 한다
  - **✨ 무한 루프를 주의하자!**

- for

  - 반복 가능(iterable)한 객체를 모두 순회하면 종료 (별도의 종료조건 필요 X)
    - string, tuple, list, range 등

  ```python
  for <변수명> in <iterable>:
      # Code block
  ```

  - 리스트 순회 - enumerate

  ```python
  friends = ['흥민', '의조', '창훈']
  ```

  

  ```python
  for idx, friend in enumerate(friends):
      print(idx, friend)
  
  0 흥민
  1 의조
  2 창훈
  ```

  

- 반복 제어
  - break, continue, for-else
  - pass vs continue

