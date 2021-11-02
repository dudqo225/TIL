# JavaScript | Conditions & Loops

### 목차

> - 조건문
> - 반복문

<br>

## 조건문

### If statement

- 조건 표현식 결과값을 Boolean 타입으로 변환 후 참/거짓 판단
- `if`, `else if`, `else`
- 조건은 소괄호(`()`) 안에 작성
- 실행할 코드는 중괄호(`{}`) 안에 작성
- 블록 스코프 생성

```javascript
// if문 기본 구조
if (condition) {
    // do something
} else if (condition) {
    // do something
} else {
    // do something
}
```

```javascript
// 예시
const nation = 'Korea'

if (nation === 'Korea') {
    console.log('안녕하세요')
} else if (nation === 'France') {
    console.log('Bonjour!')
} else {
    console.log('Hello!')
}
```



### Switch statement

- 조건 표현식 결과값이 어느 값(case)에 해당하는지 판별
- 특정 변수의 값에 따라 조건을 분기할 때 활용
- 조건이 많아질 경우 if문보다 가독성이 나을 수 있음
- **표현식의 결과값을 이용한 조건문**
- **표현식 결과값과 case문의 오른쪽 값을 비교**

- `break`, `default` 문은 선택적으로 사용 가능
- break문이 없는 경우, break문을 만나거나 default 문을 실행할 때 까지 다음 조건문을 계속 실행
- 블록 스코프 생성

```javascript
// switch문 기본 구조
switch(expression) {
    case 'first value': {
        // do something
        [break]
    }
    case 'second value': {
        // do something
        [break]
    }
    [default: {
        // do something
    }]
}
```

```javascript
// 예시 1
const nation = 'Korea'

switch(nation) {
    case 'Korea': {
        console.log('안녕하세요!')
        break
    }
    case 'France': {
        console.log('Bonjour!')
        break
    }
    default: {
        console.log('Hello!')
    }
}

/*
각 case문에 break가 없다면 default문을 만날 때까지 모든 코드가 실행된다.
*/
```

<br>

## 반복문

### while

- 조건문이 참인 동안 반복 시행
- 조건은 소괄호(`()`) 안에 작성
- 실행할 코드는 중괄호(`{}`) 안에 작성
- 블록 스코프 생성

```javascript
let i = 0

while (i < 6) {
    console.log(i) // 0, 1, 2, 3, 4, 5
    i += 1
}
```



### for

- 세미콜론(`;`)으로 구분되는 3 부분으로 작성
- **initialization**
  - 최초 반복문 진입시 1회만 실행
- **condition**
  - 매 반복 시행 전 평가
- **expression**
  - 매 반복 시행 이후 평가
- 블록 스코프 생성

```javascript
// 기본 구조
for (initialization; condition; expression) {
    // do something
}
```

```javascript
// 예시
for (let i = 0; i < 6; i++) {
    console.log(i) // 0, 1, 2, 3, 4, 5
}
```



### for... in

- **객체(object)의 속성들을 순회**할 때 사용
- 배열도 순회는 가능하지만 권장하지 않음
- 실행할 코드는 중괄호(`{}`) 안에 작성
- 블록 스코프 생성

```javascript
// 기본 구조
for (variable in object) {
    // do something
}
```

```javascript
// 예시
const capitals = {
    Korea: '서울',
    France: '파리',
    USA: '워싱턴 D.C.'
}

for (let capital in capitals) {
    console.log(capital) // Korea, France, USA
}
```



### for... of

- **반복 가능한(iterable) 객체를 순회**하며 값을 꺼낼 때 사용
  - 배열(Array) 같은 애들 원소 순회할 때 사용!
- 실행할 코드는 중괄호(`{}`) 안에 작성
- 블록 스코프 생성

```javascript
// 기본 구조
for (variable of iterables) {
    // do something
}
```

```javascript
// 예시
const fruits = ['딸기', '바나나', '멜론']

for (let fruit of fruits) {
    console.log(fruit) // 딸기, 바나나, 멜론
}
```



### 조건문 & 반복문 정리

|  키워드   |  종류  |      연관 키워드      | 스코프 |
| :-------: | :----: | :-------------------: | :----: |
|    if     | 조건문 |           -           |  블록  |
|  switch   | 조건문 | case, break, default  |  블록  |
|   while   | 반복문 |    break, continue    |  블록  |
|    for    | 반복문 |    break, continue    |  블록  |
| for... in | 반복문 |       객체 순회       |  블록  |
| for... of | 반복문 | 배열 등 Iterable 순회 |  블록  |

