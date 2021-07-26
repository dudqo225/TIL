# python | Data Structure (데이터 구조)

> ***Niklaus Wirth***
>
> "**A**lgorithm + **D**ata Structures = **P**rograms"



## 데이터 구조

- 데이터에 편리하게 접근, 변경하기 위해 데이터를 저장하거나 조작하는 법

- **순서가 있는** 데이터 구조
  - 문자열 (String)
  - 리스트 (List)
- **순서가 없는** 데이터 구조
  - 세트 (Set)
  - 딕셔너리 (Dictionary)

***

### 문자열

- 문자들의 나열 (Sequence of Characters)

- 특징

  - 변경할 수 없고 (Immutable)

  ```python
  word = '안녕하세요.'
  word[-1] = '!'
  # TypeError 발생
  ```

  - 순서가 있고 (Ordered)
  - 순회 가능한 (Iterable)

- 인덱스 (Index)

|       | a    | b    | c    |
| ----- | ---- | ---- | ---- |
| index | 0    | 1    | 2    |
| index | -3   | -2   | -1   |

- 자르기 (Slicing)

  - `s[start:stop:step]`

  |       | a    | b    | c    | d    | e    |
  | ----- | ---- | ---- | ---- | ---- | ---- |
  | index | 0    | 1    | 2    | 3    | 4    |
  | index | -5   | -4   | -3   | -2   | -1   |

  - `s[::]` : `s[0:len(s):1]` 과 동일
  - `s[::-1]` : `s[-1:-(len(s)):-1]` 과 동일
    - '뒤집기' 에 사용할 수 있다.

- 메서드 (Method)

  - 조회 / 탐색
    - `.find(x)` : x의 첫 번째 위치를 반환. 없으면 -1을 반환
    - `.index(x)` : x의 첫 번째 위치를 반환. 없으면 `ValueError` 를 일으킨다

  - 변경

    - `.replace(old, new[,count])` 

      - 바꿀 대상 글자`old` 를 새로운 글자`new` 로 바꿔서 반환 (복사본을 반환)
      - `count` 를 지정하면, 해당 개수만큼만 시행

    - `.strip([chars])` 

      - 특정한 문자를 지정하면 → 양쪽제거`strip`, 왼쪽제거`lstrip`, 오른쪽제거`rstrip`
      - 문자열을 지정하지 않으면 공백을 제거

    - `.split([chars])` : 문자열을 특정한 단위로 나눠서 리스트로 반환

    - `'separator'.join([iterable])`

      - 반복가능한(iterable) 컨테이너 요소들을 구분자(separator)로 합쳐서 문자열을 반환

      ```python
      '!'.join('hello')
      # 'h!e!l!l!o!'
      ```

      ```python
      ' '.join(['3', '7'])
      # '3 7'
      ```

    - `.capitalize()` : 앞글자를 대문자로

    - `.title()` : `'` 나 `공백`  이후를 대문자로

    - `.upper()` : 모두 대문자로 변경

    - `lower()` : 모두 소문자로 변경

    - `swapcase()` : 대 ↔ 소문자로 변경

  - 검증 : `return` 값이 반드시 `True` or `False`

    - `.isalpha()` : 알파벳 문자 여부 (*단순한 알파벳이 아닌 유니코드 상 Letter. 한국어도 포함)
    - `.isupper()` : 대문자 여부
    - `.islower()` : 소문자 여부
    - `.istitle()` : 타이틀 형식 여부
    - `.isdecimal()` ⊆ `.isdigit()` ⊆ `.isnumeric()`

***

### 리스트

- 순서가 있는 시퀀스, 인덱스로 접근

- 특징

  - 변경 가능하고 (Mutable)
  - 순서가 있고 (Ordered)
  - 순회 가능한 (Iterable)

- 메서드(Method)

  - 값 추가 및 삭제

    - `.append(x)` : 리스트에 값을 추가
    - `.extend(iterable)` : 리스트에 iterable의 항목을 추가
    - `.insert(i, x)` : 정채진 위치 `i` 에 값 `x`를 추가함.
    - `.remove(x)` : 리스트에서 값이 `x`인 첫 번째 항목을 삭제
    - `.pop(i)`
      - 정해진 위치 `i` 에 있는 값을 삭제하고, 그 항목을 반환
      - `i` 가 지정되지 않으면, 마지막 항목을 삭제하고 반환
    - `.clear()` : 모든 항목을 삭제함. 리스트 자체를 없애는 것은 아니다.

  - 탐색 및 정렬

    - `.index(x)` : `x` 값을 찾아 해당 `index` 값을 반환
    - `.count(x)` : 원하는 값 `x`의 개수를 반환
    - `.sort()` : 원본 리스트를 정렬. `None` 을 반환. `sorted` 함수와 비교!!

    ```python
    # .sort() 원본을 변경. None 반환
    n_list = [4, 3, 6, 1]
    result = n_list.sort()
    print(n_list, result)
    # [1, 3, 4, 6] None
    
    # sorted() 원본 변경 X. 정렬된 리스트 반환
    result = sorted(n_list)
    print(n_list, result)
    # [4, 3, 6, 1] [1, 3, 4, 6]
    ```

    

    - `.reverse()` : 순서를 반대로 뒤집음 (정렬하는 것은 X)

  - 복사

    - 리스트 복사는 같은 리스트의 주소 `id` 를 참조!

    - 얕은 복사 (shallow copy) 1

      - Slice 연산자를 활용하여 같은 원소를 가진 리스트이지만 다른 주소를 가진 리스트로 복사

      ```python
      a = [1, 2, 3]
      b = a[:] # 다른 주소 id 를 갖는 리스트로 복사
      print(a, b) # [1, 2, 3] [1, 2, 3]
      b[0] = 4
      print(a, b) # [1, 2, 3] [4, 2, 3]
      ```

    - 얕은 복사 (shallow copy) 2

      - `list()` 를 활용하여 같은 원소를 가진 리스트이지만 다른 주소를 가진 리스트로 복사

      ```python
      a = [1, 2, 3]
      b = list(a) # 다른 주소 id 를 갖는 리스트로 복사
      print(a, b) # [1, 2, 3] [1, 2, 3]
      b[0] = 4
      print(a, b) # [1, 2, 3] [4, 2, 3]
      ```

    - 얕은 복사 주의사항

      - 복사하는 리스트의 원소가 주소를 참조하는 경우
      - 리스트 안의 리스트는 다른 주소로 복사되지 않는다. (같은 `id` 를 참조)

      ```python
      a = [1, 2, ['a', 'b']]
      b = a[:]
      print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
      b[2][0] = 0
      print(a, b) # [1, 2, [0, 'b']] [1, 2, [0, 'b']]
      ```

    - 깊은 복사 (deep copy)

    ```python
    import copy
    
    a = [1, 2, ['a', 'b']]
    b = copy.deepcopy(a)
    print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
    b[2][0] = 0
    print(a, b) # [1, 2, ['a', 'b']] [1, 2, [0, 'b']]
    ```

- List comprehension

  - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 생성하는 방법

  ```python
  [<expression> for <변수> in <iterable>]
  [<expression> for <변수> in <iterable> if <조건식>]
  ```

  - 예시

  ```python
  # 1 ~ 3의 세제곱 리스트 생성
  cubic_list = []
  for n in range(1, 4):
      cubic_list.append(n ** 3)
  cubic_list
  
  [결과]
  [1, 8, 27]
  ```

  ```python
  # List comprehension으로 리스트 생성
  [n**3 for n in range(1, 4)]
  
  [결과]
  [1, 8, 27]
  ```

  ***

  ```python
  # 1 ~ 3 숫자 중 짝수만 담긴 리스트 생성
  even_list = []
  for i in range(1, 4):
      if i % 2 == 0:
          even_list.append(i)
  print(even_list)
  
  [결과]
  [2]
  ```

  ```python
  # List comprehension으로 리스트 생성
  [x for x in range(1, 4) if x % 2 == 0]
  
  [결과]
  [2]
  ```

  ***

  ```python
  # 실습
  girls = ['jane', 'ashley']
  boys = ['justin', 'eric']
  
  pair = []
  for boy in boys:
      for girl in girls:
          pair.append((boy, girl))
          
  ###############################################
  
  # List comprehension 으로 표현
  [(boy, girl) for boy in boys for girl in girls]
  ```

  - List comprehension 으로 표현할 때 가독성이 떨어질 수 있음을 고려해야 함.

- Built-in Function

  - `map(function, iterable)`
    - 순회 가능한 데이터 구조(iterable)의 모든 요소에 함수(function)를 적용하고, 그 결과를 `map object`로 반환
    - `list()` 형변환을 통해 결과를 직접 확인해야 함.
    - 활용 사례 : 알고리즘 문제 풀이시 `input` 값들을 숫자로 바로 활용하고 싶을 때
  - `filter(function, iterable)`
    - 순회 가능한 데이터 구조(iterable)의 모든 요소에 함수(function)를 적용하고, 그 결과가 `True` 인것들을 `filter object` 로 반환
    - `list()` 형변환을 통해 결과를 직접 확인해야 함.
  - `.zip(*iterables)`
    - 복수의 iterable을 모아 튜플을 원소로 하는 `zip object`를 반환
    - `list()` 형변환을 통해 결과를 직접 확인해야 함.

***

### 세트

- 중복 없이 순서가 없는 데이터 구조
- 특징
  - 변경 가능하고 (Mutable)
  - 순서가 없고 (Unordered)
  - 순회 가능한 (Iterable)
- 메서드(Method)
  - `.add(elem)` : 세트에 값을 추가
  - `.update(*others)` : 여러 값을 추가
  - `.remove(elem)` : 세트에서 삭제하고, 없으면 `KeyError` 발생
  - `.discard(elem)` : 세트에서 삭제하고, 없어도 에러가 발생하지 않음
  - `.pop()` : 임의의 원소를 제거하고 반환

***

### 딕셔너리

- `key` 와 `value` 로 구성된 데이터 구조

- 특징

  - 변경 가능하고 (Mutable)
  - 순서가 없고 (Unordered)
  - 순회 가능한 (Iterable)

- 메서드(Method)

  - 조회

    - `.get(key[,default])`
      - `key`를 통해 `value`를 가져옴
      - `KeyError`가 발생하지 않으며, default 값을 설정할 수 있음 (기본 : `None`)

  - 추가 및 삭제

    - `.pop(key[,default])`

      - `key` 가 딕셔너리에 있으면 제거하고 해당 `value` 값을 반환
      - 그렇지 않으면 default를 반환
      - default 값이 없으면 `KeyError` 발생

    - `.update()`

      - 값을 제공하는 `key`, `value`로 덮어 씀

      ```python
      my_dict = {'apple': '사', 'banana': '바나나'}
      my_dict.update(apple='사과')
      print(my_dict) # {'apple': '사과', 'banana': '바나나'}
      ```

- 딕셔너리 순회

  - 딕셔너리는 기본적으로 `key` 를 순회하며, `key` 를 통해 값을 활용

  ```python
  grades = {'son': 90, 'park': 80}
  for student in grades:
      print(student)
  
  [결과]
  son
  park
  
  for student in grades:
      print(student, grades[student])
      
  [결과]
  son 90
  park 80
  ```

  - 추가 메서드

    - `keys()` : `key` 로 구성된 결과
    - `values()` : `value` 로 구성된 결과
    - `items()` : `(key, value)` 의 튜플로 구성된 결과

    ```python
    grades = {'son': 90, 'park': 80}
    for name, score in grades.items():
        print(name, score)
        
    [결과]
    son 90
    park 80
    ```

- Dictionary Comprehension

  - 표현식 & 문장

  ```python
  {key: value for <변수> in <iterable>}
  {key: value for <변수> in <iterable> if <조건식>}
  ```

  - 예시

  ```python
  dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45}
  
  result = {}
  for key, value in dusts.items():
      if value > 70:
          resutlt[key] = value
  print(result)
  
  [결과]
  {'서울': 72, '대전': 82}
  
  ######################################################
  
  # Dictionary Comprehension 으로 표현
  {key: value for kye, value in dusts.items() if value > 70}
  
  [결과]
  {'서울': 72, '대전': 82}
  ```

  



