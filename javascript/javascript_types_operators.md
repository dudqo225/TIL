# JavaScript | Types & Operators

### 목차

> - 데이터 타입
> - 연산자

<br>

## 데이터 타입

### 원시 타입 (Primitive Type)

- 객체 (object) 가 아닌 기본 타입
- 변수에 해당 타입의 값이 담김
- 다른 변수에 복사할 때 실제 값이 복사됨
  - **Number**
    - 정수, 실수 구분 없는 하나의 숫자 타입
    - 부동소수점 형식을 따름
    - NaN (Not-A-Number)
      - 계산 불가능한 경우 반환되는 값
  - **String**
    - 텍스트 데이터
    - 16비트 유니코드 문자의 집합
    - 작은 따옴표 / 큰 따옴표 사용
    - **템플릿 리터럴 (Template Literal)**
      - ES6부터 지원
      - 따옴표 대신 backtick(``)으로 표현
      - `${ expression }`  형태로 표현식 삽입 가능
  - **Boolean**
    - 논리적 참/거짓
    - true 또는 false로 표현 (대문자 아님 주의!)
    - 조건문이나 반복문에서 유용하게 사용
  - **undefined**
    - **값이 없음**을 나타냄
    - 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 undefined가 할당됨
  - **null**
    - **값이 없음**을 의도적으로 표현할 때 사용
    -  `typeof` 연산자
      - 자료형 평가를 위한 연산자
      - null은 원시 타입이지만, typeof 연산자의 결과는 객체(object)로 표현됨
  - Symbol

##### undefined vs. null

- 둘 다 빈 값을 표현하기 위한 데이터 타입
- null은 개발자가 의도적으로 필요한 경우 할당 / undefined는 변수 선언이 아무 값이 할당되지 않으면 JS가 자동으로 할당
- typeof 연산자의 결과 null은 object, undefined는 undefined

##### 자동 형변환 (ToBoolean Conversions)

| 데이터 타입 |    거짓    |        참        |
| :---------: | :--------: | :--------------: |
|  Undefined  | 항상 거짓  |        -         |
|    Null     | 항상 거짓  |        -         |
|   Number    | 0, -0, NaN | 나머지 모든 경우 |
|   String    | 빈 문자열  | 나머지 모든 경우 |
|   Object    |     -      |     항상 참      |

<br>

### 참조 타입 (Reference Type)

- 객체 (object) 타입의 자료형
- 변수에 해당 객체의 참조 값이 담김
- 다른 변수에 복사할 때 참조값이 복사됨
  - Objects
  - Array
  - Function
  - etc.

<br>

## 연산자

### 할당 연산자

```javascript
let x = 0

x += 10
console.log(x) // 10

x -= 10
console.log(x) // 7

x *= 10
console.log(x) // 70

x /= 10
console.log(x) // 7

x++            // += 연산자와 동일
console.log(x) // 8

x--            // -= 연산자와 동일
console.log(x) // 7
```



### 비교 연산자

```javascript
const numOne = 1
const numTwo = 100
console.log(numOne < numTwo) // true

const charOne = 'a'
const charTwo = 'z'
console.log(char > charTwo) // false

/*
알파벳끼리 비교할 경우
알파벳 순서상 후순위가 더 크다
소문자가 대문자보다 더 크다
*/
```



### 동등 비교 연산자 (==)

```javascript
const a = 1004
const b = '1004'
console.log(a == b) // true

const c = 1
const d = true
console.log(c == d) // true

// 자동 타입 변환
console.log(a + b) // 10041004
console.log(c + d) // 2

/*
암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
두 피연산자가 모두 객체일 경우, 메모리의 같은 객체를 바라보는지 판별
예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용 X
*/
```



### 일치 비교 연산자 (===)

```javascript
const a = 1004
const b = '1004'
console.log(a === b) // false

const c = 1
const d = true
console.log(c === d) // false

/* 
엄격한 비교가 이루어지며, 암묵적 타입 변환이 발생하지 않음
타입과 값 모두 같은지 비교하는 방식
두 피연산자가 모두 객체일 경우, 메모리의 같은 객체를 바라보는지 판별
*/ 
```



### 논리 연산자

```javascript
// and 연산
console.log(true && false)  // false
console.log(true && true)   // true
console.log(1 && 0)         // 0
console.log(4 && 7)         // 7
console.log('' && 5)        // ''

// or 연산
console.log(true || false)  // true
console.log(false || false) // false
console.log(1 || 0)         // 1
console.log(4 || 7)         // 4
console.log('' || 5)        // 5

// not 연산
console.log(!true)          // false
console.log(!'Hello!')      // false

// 단축 평가를 지원 (파이썬과 같은 개념인듯?)
```



### 삼항 연산자 (Ternary Operator)

```javascript
console.log(true ? 1 : 2)  // 1
console.log(false ? 1 : 2) // 2

const result = Math.PI > 4 ? 'Yes' : 'No'
console.log(result)        // No
```

- 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 왼쪽의 조건식이 참이면 콜론(`:`) 앞의 값을, 그렇지 않으면 콜론(`:`) 뒤의 값을 사용
- 삼항 연산자 결과는 변수에 할당 가능

- 한 줄에 표기하는 것을 권장

