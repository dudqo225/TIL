# JavaScript | Variables & Identifiers

### 목차

> - 변수와 식별자

<br>

## 변수와 식별자

### 식별자 정의와 특징

- **식별자(identifier)**는 **변수를 구분할 수 있는 변수명**을 말함
- 식별자는 반드시 **문자, 달러(`$`), 밑줄(`_`)** 로 시작
- **대소문자를 구분**, 클래스명 이외에는 모두 소문자로 시작
- 예약어 사용 불가능 (파이썬이나 자바, 기타 다른 프로그래밍 언어와 동일)
  - 예약어: `for`, `if`, `else` 등

### 식별자 작성 스타일

- 카멜 케이스 (camelCase, lower-camel-case)
  - 변수, 객체, 함수에 사용

```javascript
// 변수
let dog
let variableName

// 객체
const userInfo = { name: 'john', age: 30 }

// 함수
function getPropertyName () {}
function onClick () {}
```

- 파스칼 케이스 (PascalCase, upper-camel-case)
  - 클래스, 생성자에 사용

```javascript
// 클래스
class User {
    constructor(options) {
        this.name = options.name
    }
}

// 생성자
const good = new User({
    name: '홍길동', 
})
```

- 대문자 스네이크 케이스 (SNAKE_CASE)
  - 상수(constants)에 사용

```javascript
// 상수
const API_KEY = 'KEY'
const PI = Math.PI

// 상수가 아닌 경우
const mutableCollection = new Set()
```

<br>

### 변수 선언 키워드

- `let`
  - **재할당 할 수 있는** 변수 선언시 사용
  - 변수 **재선언 불가능**
  - 블록 스코프
- `const`
  - **재할당 할 수 없는** 변수 선언시 사용
  - 변수 **재선언 불가능**
  - 블록 스코프
- `var`
  - **재할당 및 재선언 모두 가능**
  - ES6 이전에 변수를 선언할 때 사용되던 키워드
  - 호이스팅 되는 특성으로 인해 예기치 못한 문제 발생 가능
  - 함수 스코프



##### 호이스팅 (hoisting)

- 변수를 선언 이전에 참조할 수 있는 현상
- 변수 선언 이전의 위치에서 접근시 `undefined`를 반환

```javascript
console.log(username) // undefined
var username = '손흥민'

console.log(email)    // Uncaught ReferenceError
let email = 'son@gmail.com'

console.log(age )     // Uncaught ReferenceError
const age = 30
```



##### 블록 스코프 (block scope)

- if, for, 함수 등의 중괄호 내부
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

```javascript
let x = 1

if (x === 1) {
    let x = 2
    console.log(x) // 2
}

console.log(x)	   // 1
```

##### 함수 스코프 (function scope)

- 함수의 중괄호 내부
- 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

```javascript
function foo() {
    var x = 5
    console.log(x)  // 5
}

// ReferenceError: x is not defined
console.log(x)
```



#### 선언, 할당, 초기화

- 선언 (Declaration)
  - 변수를 생성하는 행위 또는 시점
- 할당 (Assignment)
  - 선언된 변수에 값을 저장하는 행위 또는 시점
- 초기화 (Initialization)
  - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```javascript
let foo				// 선언
console.log(foo)	// undefined

foo = 11			// 할당
console.log(foo)	// 11

let bar = 0			// 선언 + 할당
console.log(bar)	// 0
```



#### let, const, var 비교

| 키워드 | 재선언 | 재할당 |   스코프    |     비고     |
| :----: | :----: | :----: | :---------: | :----------: |
|  let   |   X    |   O    | 블록 스코프 | ES6부터 도입 |
| const  |   X    |   X    | 블록 스코프 | ES6부터 도입 |
|  var   |   O    |   O    | 함수 스코프 |    사용 x    |

