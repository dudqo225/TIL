# JavaScript | Arrays & Objects

### 목차

> - 배열 (Arrays)
> - 객체 (Objects)

<br>

## 배열 (Arrays)

### 정의 및 특징

- 키와 속성을 담고 있는 참조 타입의 객체 (Object)
- 순서를 보장
- 주로 대괄호(`[]`)를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 `array.length` 형태로 접근 가능
- 배열의 마지막 원소는 `array.length-1` 로 접근

```javascript
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])     // 1
console.log(numbers[-1])    // undefined
console.log(numbers.length) // 5

console.log(numbers[numbers.length - 1]) // 5
```



### 주요 메서드 - 기본편

##### 참고

> [MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array#%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4_%EB%A9%94%EC%84%9C%EB%93%9C)
>
> [ECMA262](https://tc39.es/ecma262/#sec-properties-of-the-array-constructor)

|     메서드      |                       설명                       |            비고            |
| :-------------: | :----------------------------------------------: | :------------------------: |
|     reverse     |      원본 배열의 요소들 순서를 반대로 정렬       |                            |
|   push & pop    |        배열의 가장 뒤 요소를 추가 / 제거         |                            |
| unshift & shift |        배열의 가장 앞 요소를 추가 / 제거         |                            |
|    includes     | 배열에 특정 값이 존재하는지 판별 후 참/거짓 반환 |                            |
|     indexOf     | 배열에 특정 값이 존재하는지 판별 후 인덱스 반환  |   요소가 없으면 -1 반환    |
|      join       |    배열의 모든 요소를 구분자를 이용하여 연결     | 구분자 생략시 쉼표(,) 기준 |



### 주요 메서드 - 심화편

- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 **callback 함수** 를 받는 것이 특징임
  - callback 함수란?
    - 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수

| 메서드  |                             설명                             |   비고   |
| :-----: | :----------------------------------------------------------: | :------: |
| forEach |         배열 각 요소에 대해 콜백 함수를 한번 씩 실행         | 반환값 X |
|   map   |      콜백 함수의 반환값을 요소로 하는 새로운 배열 반환       |          |
| filter  | 콜백 함수의 반환값이 참인 요소들만 모아서 새로운 배열을 반환 |          |
| reduce  |     콜백 함수의 반환값들을 하나의 값(acc)에 누적 후 반환     |          |
|  find   |          콜백 함수의 반환값이 참이면 해당 요소 반환          |          |
|  some   |    배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환    |          |
|  every  |      배열의 모든 요소가 판별 함수를 통과하면 참을 반환       |          |



##### forEach

- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 3가지 매개변수로 구성
  - element : 배열의 요소
  - index : 배열 요소의 인덱스
  - array : 배열 자체
- **반환 값(return)이 없는 메서드**

```javascript
// 기본 구조
array.forEach((element, index, array) => {
    // do something
})

// 예시
const location = ['서울', '대전', '대구', '부산', '인천']

location.forEach((region, index) => {
    console.log(region, index)
    // 서울 0
    // 대전 1
    // 대구 2
    // 부산 3
    // 인천 4
})
```



##### map

- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 **함수 반환 값을 요소로 하는 새로운 배열** 반환
- 기존 배열 전체를 다른 형태로 바꿀 때 유용

```javascript
// 기본 구조
array.map((element, index, array) => {
    // do something
})

// 예시
const numbers = [1, 2, 3, 4, 5]

const doubleNums = numbers.map((num) => {
    return num * 2
})
console.log(doubleNums) // [2, 4, 6, 8, 10]
```



##### filter

- 배열 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 **함수 반환 값이 참인 요소만 모아서 새로운 배열**을 반환
- 기존 배열 요소들을 필터링할 때 유용

```javascript
// 기본 구조
array.filter((element, index, array) => {
    // do something
})

// 예시
const numbers = [1, 2, 3, 4, 5]

const oddNums = numbers.filter((num, index) => {
    return num % 2
})
console.log(oddNums) // 1, 3, 5
```



##### reduce

- 배열 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 **함수 반환 값들을 하나의 값(acc)에 누적 후 반환**
- 주요 매개변수
  - **acc**
    - 이전 callback 함수의 반환 값이 누적되는 변수
  - **initialValue** (optional)
    - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫번째 값
  - 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

```javascript
// 기본 구조
array.reduce((acc, element, index, array) => {
    // do something
}, initialValue)

// 예시
const numbers = [1, 2, 3]

const result = numbers.reduce((acc, num) => {
    return acc + num
}, 0)

console.log(result) // 6
```



##### find

- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 **함수 반환 값이 참이면 해당 요소를 반환**
- 찾는 값이 배열에 없으면 **undefined** 반환

```javascript
// 기본 구조
array.find((element, index, array) => {
    // do something
})

// 예시
const players = [
    { name: '손흥민', age: 30 },
	{ name: '황의조', age: 29 },
    { name: '박지성', age: 35 },
]

const result = players.find((player) => {
    return player.name === '손흥민'
})
console.log(result) // { name: '손흥민', age: 30 }
```



##### some

- **배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환**
- 모든 요소가 통과하지 못하면 거짓 반환
- **빈 배열은 항상 거짓** 반환

```javascript
// 기본 구조
array.some((element, index, array) => {
    // do something
})

// 예시
const numbers = [1, 3, 5, 7, 9]

const hasEvenNum = numbers.some((num) => {
    return num % 2 === 0
})
console.log(hasEvenNum) // false

const has OddNum = numbers.some((num) => {
    return num % 2
})
console.log(hasOddNum) // true
```



##### every

- **배열 모든 요소가 주어진 판별 함수를 통과하면 참을 반환**
- 모든 요소가 통과하지 못하면 거짓 반환
- **빈 배열은 항상 참** 반환

```javascript
// 기본 구조
array.every((element, index, array) => {
    // do something
})

// 예시
const numbers = [2, 4, 6, 8, 10]

const isEveryNumberEven = numbers.every((num) => {
    return num % 2 === 0
})
console.log(isEveryNumberEven) // true

const isEveryNumberOdd = numbers.every((num) => {
    return num % 2
})
console.log(isEveryNumberOdd) // false
```



### 배열 순회 방법 비교

|   방식    |                             특징                             |             비고             |
| :-------: | :----------------------------------------------------------: | :--------------------------: |
|    for    | 모든 브라우저 환경에서 지원<br>인덱스를 활용하여 배열의 요소에 접근<br>break, continue 사용 가능 |                              |
| for... of | 일부 오래된 브라우저 환경에서 지원 X<br/>인덱스 없이 배열의 요소에 바로 접근 가능<br/>break, continue 사용 가능 |                              |
|  forEach  | 대부분 브라우저 환경에서 지원<br>break, continue 사용 불가능 | Airbnb Style Guide 권장 방식 |

<br>

## 객체 (Objects)

### 정의와 특징

- 객체는 **속성(Property)의 집합**이며, 중괄호 내부에 **key-value 쌍**으로 표현됨
- **key**
  - 문자열 타입만 가능
  - 이름에 띄어쓰기 등 구분자가 있으면 따옴표로 묶어서 표현
- **value**
  - 모든 타입 가능
- 객체 요소 접근은 점(`.`) 또는 대괄호(`[]`)
  - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능



#### ES6 문법 (1) - 속성명 축약 (shorthand)

- 객체를 정의할 때 **key와 할당하는 변수의 이름이 같으면 축약 가능**

```javascript
// 축약 없는 코드 (ES5)
let books = ['수학의 정석', '과학의 정석']
let magazines = null

var bookShop = {
    books: books,
    magaznies: magazines,
}
console.log(bookShop.books) // ['수학의 정석', '과학의 정석']

// 축약 문법 사용 (ES6)
var bookShop = {
    books,
    magaznies,
}
```



#### ES6 문법 (2) - 메서드명 축약 (shorthand)

- **메서드 선언 시 `function` 키워드 생략 가능**

```javascript
// ES5
var obj = {
    greeting: function () {
        console.log('Hi!')
    }
}
obj.greeting() // Hi!

// 축약 문법 사용 (ES6)
const newObj = {
    greeting() {
        console.log('Hi!')
    }
}
newObj.greeting() // Hi!
```



#### ES6 문법 (3) - 계산된 속성 (computed property name)

- 객체를 정의할 때 **key의 이름을 표현식을 이용해서 동적으로 생성 가능**

```javascript
const key = 'regions'
const value = ['서울', '대전', '대구', '부산']

const city = {
    [key]: value,
}

console.log(city)         // { regions: Array(4)}
console.log(city.regions) // ['서울', '대전', '대구', '부산']
```



#### ES6 문법 (4) - 구조 분해 할당 (destructing assignment)

- **배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당**할 수 있는 문법

```javascript
// 기본
const userInfo = {
    name: '홍길동',
    userId: 'gildong',
    phoneNum: '010-1234-5678',
    email: 'gildong@gmail.com'
}

const name = userInfo.name
const userId = userInfo.userId
const phoneNum = userInfo.phoneNum
const email = userInfo.email


// 구조 분해 할당
const userInfo = {
    name: '홍길동',
    userId: 'gildong',
    phoneNum: '010-1234-5678',
    email: 'gildong@gmail.com'
}

const { name } = userInfo
const { userId} = userInfo
const { phoneNum } = userInfo
const { email } = userInfo

// 여러개도 가능함
const { name, userId, phoneNum, email} = userInfo
```



### JSON (JavaScript Object Notation)

- **key - value 쌍**의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
- JS 객체와 유사하게 생겼으나 실제로는 **문자열 타입**
  - JS 객체로써 조작하기 위해서는 구문 분석(parsing)이 필요함
- 자바스크립트에서는 JSON을 조작하기 위한 2가지 내장 메서드 제공
  - `JSON.parse()`
    - JSON => 자바스크립트 객체
  - `JSON.stringify()`
    - 자바스크립트 객체 => JSON