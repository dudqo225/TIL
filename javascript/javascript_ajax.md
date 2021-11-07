# JavaScript | AJAX

### 목차

> - AJAX
> - Asynchronous JavaScript
>   - Callback Function
>   - Promise
>   - Axios

<br>

## AJAX

#### AJAX란?

- **A**synchronous **J**avaScript **A**nd **X**ML (비동기식 JavaScript와 XML)
- 서버와 통신하기 위해 `XMLHttpRequest` 객체 활용
- JSON, XML, HTML, 일반 텍스트 형식 등 다양한 포맷을 주고 받을 수 있음

#### 특징

- 페이지 전체를 새로고침(reload) 하지 않고서도 수행되는 **비동기성**
  - 사용자 event를 통해 전체 페이지가 아닌 일부분만을 업데이트 할 수 있음
- 페이지 새로고침 없이 서버에 요청 → 서버로부터 데이터를 받고 작업을 수행

#### 배경

- 2005년 Google Maps & Gmail 등에 활용되는 기술을 설명하기 위해 AJAX 용어 최초 사용
- AJAX는 특정 기술이 아닌 기존의 여러 기술을 사용하는 새로운 접근법을 설명하는 용어
- Google 사용 예시
  - Gmail
    - 메일 전송 요청이 처리되기 전 다른 페이지로 넘어가더라도 메일은 전송 됨
  - Maps
    - 스크롤 행위 하나하나가 모두 요청이지만 페이지가 갱신(reload)되지 않음

#### XMLHttpRequest 객체

- 서버와 상호작용하기 위해 사용되며 전체 페이지의 새로고침 없이 데이터를 받아올 수 있음
- 사용자의 작업을 방해하지 않으면서 페이지 일부를 업데이트 할 수 있음
- 주로 AJAX 프로그래밍에 사용
- XML 외에 모든 종류의 데이터를 받아올 수 있음
- 생성자
  - `XMLHttpRequest()`



## Asynchronous JavaScript

#### 동기식

- 순차적, 직렬적 Task 수행
- 요청을 보낸 후 응답을 받아야만 다음 동작이 이루어짐 (blocking)

#### 비동기식

- 병렬적 Task 수행
- 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐 (non-blocking)

##### 비동기를 사용하는 이유?

- 사용자 경험
  - 매우 큰 데이터를 동반하는 앱이 있다고 가정
  - 동기식 코드일 경우, 데이터를 모두 불러온 뒤 앱이 실행됨
  - 비동기식 코드라면 데이터를 요청하고 응답받는 동안, 앱 실행을 함께 진행
  - 많은 웹 API 기능은 비동기 코드를 사용하여 실행

##### JavaScript는 Single Threaded

- 컴퓨터가 여러개 CPU를 가지고 있어도 Main Thread라 불리는 단일 스레드에서만 작업을 수행
- 이벤트를 처리하는 Call Stack이 하나인 언어라는 의미
  - 즉시 처리하지 못하는 이벤트들을 Web API로 보내서 처리
  - 처리된 이벤트들은 처리된 순서대로 Task Queue에 줄을 세워 놓고
  - Call Stack이 비면 Evet Loop가 대기줄(Task Queue)에서 가장 오래된 이벤트를 Call Stack으로 보냄

##### Concurrency Model (동시성 모델)

- Call Stack
  - 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack(LIFO) 형태의 자료 구조
- Web API (Browser API)
  - JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API
  - `setTimeout()`, DOM events 그리고 AJAX로 데이터를 가져오는 시간이 소요되는 일들을 처리
- Task Queue (Event Queue, Message Queue)
  - 비도익 처리된 callback 함수가 대기하닌 Queue(FIFO) 형태의 자료 구조
  - main thread가 끝난 후 실행되어 후속 JS 코드가 차단되는 것을 방지
- Event Loop
  - Call Stack이 비어있는 지 확인
  - 비어있는 경우 Task Queue에서 실행 대기 중인 callback 함수가 있는지 확인
  - 대기중인 callback 함수가 있다면 가장 앞에 있는 callback 함수를 Call Stack으로 Push

<br>

### Callback Function

- 다른 함수에 인자로 전달된 함수
- 외부 함수 내에서 호출되어 루틴/작업을 완료
- 동기식, 비동기식 모두 사용됨
  - 비동기 작업이 완료된 후 코드 실행을 계속하는 데 주로 사용됨
  - 비동기 콜백 (asynchronous callback) 이라고 함

##### JavaScript 함수는 일급 객체 (First Class Object)

- 일급 객체 (일급 함수)
  - 다른 객체들에 적용할 수 있는 연산을 모두 지원하는 객체(함수)
- 조건
  - 인자로 넘길 수 있어야 함
  - 함수의 반환 값으로 사용할 수 있어야 함
  - 변수에 할당할 수 있어야 함

##### Callback Hell

- 순차적인 연쇄 비동기 작업을 처리하기 위해 callback 함수를 반복 호출하는 패턴이 지속됨
- pyramid of doom(파멸의 피라미드)라고도 함
- 디버깅하기 어렵고 코드 가독성이 떨어짐
- 해결 방법
  - 코드의 깊이를 얕게 유지 (Keep your code shallow)
  - 모듈화 (Modularize)
  - 모든 단일 오류 처리 (Handle Every Single Error)
  - **Promise 콜백** 방식 사용 (Promise callbacks)

<br>

### Promise

#### Promise Object

- 비동기 작업의 최종 완료 / 실패를 나타내는 객체
  - 미래의 완료 / 실패와 그 결과 값을 나타냄
  - 미래의 어떤 상황에 대한 약속
- 성공(이행)에 대한 약속
  - `.then()`
- 실패(거절)에 대한 약속
  - `.catch()`

#### Methods

- 반환 값이 반드시 있어야 함
- 없으면 callback 함수가 이전의 promise 결과를 받을 수 없음

- `.then(callback)`
  - 이전 작업(promise)이 성공했을 때 수행할 작업을 나타내는 callback 함수
  - 각 callback 함수는 이전 작업의 성공 결과를 인자로 전달받음
  - 성공했을 때의 코드를 callback 함수 안에 작성
  - 각각의 `.then()` 블록은 서로 다른 promise를 반환
    - 여러 개 사용(chaining)하여 연쇄적인 작업을 수행할 수 있음
    - 비동기 작업을 차례대로 수행할 수 있다는 의미
- `.catch(callback)`
  - `.then`이 하나라도 실패하면 동작 (동기식의 try - except 구문과 유사)
  - 이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용할 수 있음
- `.finally(callback)`
  - Promise 객체를 반환
  - 결과와 상관없이 무조건 지정된 callback 함수 실행
  - 어떠한 인자도 전달받지 않음
    - Promise가 성공되었는지 실패되었는지 판단할 수 없기 때문
  - 무조건 실행되어야 하는 절에서 활용
    - `.then()`, `.catch()` 블록에서의 코드 중복을 방지

#### Promise가 보장하는 것

- callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 전에는 절대 호출되지 않음
- 비동기 작업이 성공/실패한 뒤 `.then()` 메서드를 이용하여 추가한 경우에도 위와 똑같이 동작
- `.then()` 을 여러번 사용하여 여러 개의 callback 함수를 추가할 수 있음 (Chaining)

<br>

### Axios

- "Promise based HTTP Client for the browser and Node.js"
- 브라우저를 위한 Promise 기반의 클라이언트

- XHR 객체보다 편리하고 확장성 있는 인터페이스를 라이브러리 형태로 제공

```java
// XMLHttpRequest
const request = new XMLHttpRequest()
const URL = '...'
    
request.open('GET', URL)
request.send()

const todo = request.response
console.log(todo)
    
// Axios
const URL = '...'

axios.get(URL)
    .then(response => {
        console.log(response.data)
    })
```

<br>

#### async & await

- 비동기 코드를 작성하는 새로운 방법
- 기존 promise 시스템 위에 구축된 syntactic sugar
  - promise 구조의 then chaining을 제거
  - 비동기 코드를 좀 더 동기 코드처럼 표현
  - syntactic sugar
    - 더 쉽게 읽고 표현할 수 있도록 설계된 프로그래밍 언어 내의 구문
    - 문법적 기능은 그대로 유지하되 사용자가 직관적으로 코드를 읽을 수 있게 만듦
