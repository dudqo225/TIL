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





### Callback Function

### Promise

### Axios

