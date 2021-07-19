## python_container



### 컨테이너(Container) 란?

- 여러개 값을 저장할 수 있는 객체

1. 시퀀스(sequence)형 : 순서가 있는 데이터

   - 순서가 있다 != 정렬되어 있다

   - 리스트, 튜플, 레인지, 문자형, 바이너리

   

2. 비시퀀스(non-sequence)형 : 순서가 없는 데이터

   - 세트, 딕셔너리

### 시퀀스

#### 리스트

`[]` 혹은 `list()` 로 생성



#### 튜플

`()` 혹은 `tuple()` 로 생성



#### 레인지

- 기본형 `range(n)` : 0부터 n-1까지 숫자의 시퀀스
- 범위 지정 `range(n, m)` : n부터 m-1까지 숫자의 시퀀스
- 범위 및 스텝 지정 `range(n, m, s)` : n부터 m-1까지 s만큼 증가시키는 숫자의 시퀀스



##### containment test

- 시퀀스 포함 여부 확인 : `in` / `not in`

##### concatenation(+)

- 시퀀스 간 연결
  - range는 TypeError 발생

##### 시퀀스 반복(*)

- 시퀀스를 반복
  - range는 TypeError 발생

##### Indexing(인덱싱)

- 시퀀스 특정 인덱스에 접근
  - 해당 인덱스가 없으면 IndexError 발생

##### Slicing(슬라이싱)

- 시퀀스를 특정 단위로 나눔

##### 길이

- 시퀀스의 길이 `len()`

##### count

- 시퀀스에서 특정 원소의 갯수를 셈 `.count()`
- 시퀀스에 없을 경우 0을 반환



### 비시퀀스

#### 세트

-  `{}` 혹은 `set()` 을 통해 생성
  - 빈 세트를 만들기 위해서는 무조건 `set()` 로 생성
  - 순서가 없기 때문에 별도의 값에 접근할 수 없다.
- 집합 연산이 가능
- 중복된 값 X



#### 딕셔너리

- `{}` 혹은 `dict()` 을 통해 생성
- key 를 통해서 value 에 접근
  - key 는 변경 불가능한 (immutable) 데이터만 사용 가능
    - string, integer, float, boolean, tuple, range
  - value 는 모든 값 가능



### 컨테이너 형변환

|            | string | list | tuple | range | set  | dictionary |
| :----------: | :------: | :----: | :-----: | :-----: | :----: | :--------: |
| **string**     | --- | ○ | ○ | × | ○ | × |
| **list**       | ○ | --- | ○ | × | ○ | × |
| **tuple**      | ○ | ○ | --- | × | ○ | × |
| **range**      | ○ | ○ | ○ | --- | ○ | × |
| **set**        | ○ | ○ | ○ | × | --- | × |
| **dictionary** | ○ | ○ (key만) | ○ (key만) | × | ○ (key만) | --- |



### 컨테이너 분류

1. immutable - 변경 불가능한 데이터
   - 리터럴 - number, string, bool
   - range
   - tuple
2. mutable - 변경 가능한 데이터
   - list
   - set
   - dictionary

