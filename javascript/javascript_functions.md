# JavaScript | Functions

### 목차

> - 함수 활용법
> - 선언식 vs 표현식
> - Arrow Function

<br>

## 함수 활용법

### 함수

- 참조 타입 중 하나로, function 타입에 속함
- 함수 정의 방법
  - **함수 선언식 (function declaration)**
  - **함수 표현식 (function expression)**
- JavaScript 함수는 일급 객체(First-class Citizen)에 해당
  - 일급 객체란?
    - 변수에 할당 가능
    - 함수의 매개변수로 전달 가능
    - 함수의 반환값으로 사용 가능



### 함수 선언식 (function statement, declaration)

- 함수의 이름과 함께 정의하는 방식
- 3가지 부분
  - 함수의 이름 (name)
  - 매개변수 (args)
  - 몸통 (중괄호 내부)

```javascript
// 기본 구조
function name(args) {
    // do something
}
```

```javascript
// 예시
function add(numOne, numTwo) {
    return numOne + numTwo
}

const result = add(1, 2)
console.log(result) // 3
```



### 함수 표현식 (function expression)

- 함수를 표현식 내에서 정의
  - 표현식이란? 어떤 하나의 값으로 결정되는 코드 단위
- 이름을 생략하고 **익명 함수**로 정의 가능
  - 익명함수 (anonymous function) : 이름이 없는 함수
  - **익명함수는 함수 표현식에서만 가능**
- 3가지 부분
  - 함수의 이름 (생략 가능)
  - 매개변수 (args)
  - 몸통 (중괄호 내부)

```javascript
// 기본 구조
const myFunction = function (args) {
    // do something
}
```

```javascript
// 예시
const add = function (numOne, numTwo) {
    return numOne + numTwo
}

const result = add(1, 2)
console.log(result) // 3
```



#### 기본 인자(default arguments)

- 인자 작성 시  `=`  문자 뒤에 기본 인자 선언 가능

```javascript
const greeting = function (name = 'noName') {
    console.log(`hi ${name}`)
}

greeting() // hi noName
```

<br>

## 선언식 vs 표현식

|        | 함수 선언식 (declaration)                          | 함수 표현식 (expression)     |
| ------ | -------------------------------------------------- | ---------------------------- |
| 공통점 | 데이터 타입, 함수 구성 요소 (이름, 매개변수, 몸통) |                              |
| 차이점 | 익명 함수 불가능<br>호이스팅 O                     | 익명 함수 가능<br>호이스팅 X |
| 비고   |                                                    | Airbnb Style Guide 권장 방식 |

- 함수 타입은 선언식, 표현식 모두 `function` 으로 동일
- 함수 선언식에서는 호이스팅이 발생하지만, 함수 표현식에서는 함수 정의 전에 함수를 호출시 에러가 발생함.
- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

```javascript
// 함수 표현식 참고
sub(7, 2) // Uncaught ReferenceError: Cannot access 'sub' before initialization

const sub = function (num1, num2) {
    return num1 + num2
}

console.log(sub2) // undefined
sub2(7, 2) // Uncaught TypeError: sub is not a function

var sub2 = function (num1, num2) {
    return num1 - num2
}

/*
함수 표현식을 const가 아니 var 키워드로 작성한 경우, 변수 선언 전 undefined로 초기화 되어 ReferenceError가 아닌 TypeError가 발생
*/
```

<br>

## Arrow Function

- 화살표 함수 (Arrow Function)
  - 함수를 비교적 간결하게 정의할 수 있는 문법
  - **`function` 키워드 생략 가능**
  - **매개변수가 하나 뿐이라면, `()` 도 생략 가능**
  - **몸통이 표현식 하나라면 `{}`과 `return` 생략 가능**

```javascript
// 화살표 함수 사용 예시

// 기본 함수 표현식
const arrow = function (name) {
    return `hello! ${name}`
}

// 1. function 키워드 삭제
const arrow = (name) => { return `hello! ${name}` }

// 2. () 생략
const arrow = name => { return `hello! ${name}` }

// 3. {} & return 생략
const arrow = name => `hello! ${name}`
```

