# python | Function 함수



### 함수 기본 구조

- 함수 정의 → 호출
- 함수 정의 ``def``
  - 이름 (Name)
  - 매개변수 (Parameters)
  - 함수 바디 (Fucntion Body)
  - 반환값 (Return)

- 호출/실행 `함수명( )`



### print() vs return

##### 1. print() > 출력 : 중간 과정

##### 2. return > 반환 : 결과물



### Function input

#### 1. 위치 인자(Positional Arguments)

- 함수 호출시 위치에 따라 인자가 함수에 전달됨

#### 2. 기본 인자 값(Default Arguments Values)

- 기본값을 지정하여 함수 호출 시 인자 값을 설정하지 않아도 됨

#### 3. 키워드 인자(Keyword Arguments)

- 직접 변수의 이름으로 특정 인자 전달이 가능
- 키워드 인자 다음에 위치 인자를 사용할 수 없음

#### 4. 가변 인자 리스트(Arbitrary Argument Lists)

- 임의의 갯수 인자로 호출되도록 지정
- 인자들은 튜플로 묶여 처리되고, 매개변수에 *을 붙여 표현 `*args`

#### 5. 가변 키워드 인자(Arbitrary Keyword ARguments)

- 임의의 갯수 인자를 키워드 인자로 호출되도록 지정
- 인자들은 딕셔너리로 묶여 처리되고, 매개변수에 **을 붙여 표현 `**kwargs`



### Scope (스코프) ≒ namespace (이름공간)

- 전역 스코프 (global scope) vs 지역 스코프 (local scope)
- 전역 변수 (global variable) vs 지역 변수 (local variable)



##### 이름 검색 규칙(Name Resolution)

- **LEGB Rule**
  - **L**ocal scope : 함수
  - **E**nclosed scope : 특정 함수의 상위 함수
  - **G**lobal scope : 함수 밖의 변수, Import 모듈
  - **B**uilt-in scope : 파이썬 안에 내장되어 있는 함수/속성



##### global & nonlocal

