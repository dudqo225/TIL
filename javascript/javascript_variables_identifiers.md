# JavaScript | variables & identifiers

### 목차

> - Intro to JavaScript
>
> - DOM
>
> - Event Listener

<br>

## Intro to JavaScript

- 자바스크립트의 필요성
  - 브라우저 화면을 '동적'으로 만들기 위함
  - 브라우저를 조작할 수 있는 유일한 언어

- 핵심 인물
  - 팀 버너스리 (Tim Berners-Lee)
    - www, URL, HTTP, HTML 최초 설계자
    - 웹의 아버지
  - 브랜던 아이크 (Brendan Eich)
    - JavaScript 최초 설계자
    - 모질라 재단 공동 설립자
    - 코드네임 피닉스 프로젝트 진행 (파이어폭스의 전신)

- JavaScript 탄생
  - 1994, 브랜던 아이크가 HTML을 동적으로 동작하기 위한 프로젝트를 진행하면서 JS를 개발
  - Mocha > LiveScript > JavaScript(1995)로 명칭 변경

- 파편화 & 표준화

  - 많은 브라우저에서 자체 JS 언어를 사용하게 됨
  - 서로 다른 JS로 인해 크로스 브라우징 이슈 발생 > 웹 표준의 필요성 제기

  - 1997, ECMAScript 1(ES1) 탄생
  - 2015, ES2015 (ES6) 탄생
    - JS의 고질적인 문제 해결
    - JS 다음 시대라고 불릴 정도로 많은 혁신과 변화를 맞이
    - 현재 표준 대부분이 **ES6+**

- Vanilla JavaScript
  - 크로스 브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장(jQuery 등)
  - ES6 이후, 다양한 도구의 등장으로 순수 자바스크립트의 활용 증대

<br>

## DOM

- 브라우저에서 할 수 있는 일
  - DOM 조작 - HTML 조작
  - BOM 조작 - navigator, screen, location, frames, history, XHR
  - JavaScript core (ECMAScript)
    - Data Structure(Object, Array), Conditional Expression, Iteration

#### DOM 이란?

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
- 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
- 속성 접근, 메서드 활용 외에도 프로그래밍 언어적 특성을 활용한 조작 가능
- 주요 객체
  - `window` : DOM을 표현하는 창. 가장 최상위 객체 (작성시 생략 가능)
  - `document` : 페이지 컨텐츠의 Entry Point 역할. \<body> 등과 같은 수많은 요소들을 포함
  - `navigator`, `location`, `history`, `screen`...

- **파싱 (Parsing)**
  - 구문 분석, 해석
  - 브라우저가 문자열을 해석해서 DOM Tree로 만드는 과정

#### BOM 이란?

- Browser Object Model
- JS가 브라우저와 소통하기 위한 모델
- 브라우저 창/프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분 제어 가능

<br>

### DOM 조작

- Document는 문서 한 장(HTML)에 해당하고 이를 조작
- 조작 순서
  - 선택 (Select)
  - 변경 (Manipulation)

- DOM 관련 객체의 상속 구조
  - `EventTarget`
    - `Event Listener`를 가질 수 있는 객체가 구현하는 DOM 인터페이스
  - `Node`
    - 여러가지 DOM 타입들이 상속하는 인터페이스
  - `Element`
    - Document 안의 모든 객체가 상속하는 가장 범용적인 일반 클래스
    - 부모인 Node와 그 부모인 EventTarget의 속성을 상속받음
  - `Document`
    - 브라우저가 불러온 웹페이지를 나타냄
    - DOM 트리의 진입점(Entry Point) 역할
  - `HTMLElement`
    - 모든 종류의 HTML 요소
    - 부모 element의 속성을 상속

#### DOM - 선택 메서드

- `document.querySelector(selector)`
  - 제공한 선택자와 일치하는 element 하나 선택
  - 제공한 CSS Selector를 만족하는 첫번째 element 객체를 반환 (없으면 null)
- `document.querySelectorAll(selector)`
  - 제공한 선택자와 일치하는 여러 element 선택
  - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS Selector를 인자(문자열)로 받음
  - 지정된 셀렉터에 일치하는 `NodeList`를 반환

- `getElementById(id)`, `getElementsByTagName(name)`, `getElementsByClassName(name)`
- `querySelector()`, `querySelectorAll()`을 사용하는 이유
  - id, class, tag 선택자 등 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능

- 메서드별 반환 타입
  - 단일 element
    - `getElementById()`
    - `querySelector()`
  - HTMLCollection
    - `getElementsByTagName()`
    - `getElementsByClassName()`
  - NodeList
    - `querySelectorAll()`

##### HTMLCollection & NodeList

- 배열과 같이 각 항목에 접근하기 위한 index를 제공 (유사 배열)
- HTMLCollection
  - name, id, index 속성으로 각 항목에 접근 가능
- NodeList
  - index로만 항목에 접근 가능
  - HTMLCollection과 달리 배열에서 사용하는 `forEach` 함수 및 다양한 메서드 사용 가능
- Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만, `querySelectorAll()`에 의해 반환되는 NodeList는 Static Collection으로 실시간 반영되지 않음

##### Collection

- LiveCollection
  - 문서가 바뀔 때 실시간으로 업데이트
  - DOM의 변경사항을 실시간으로 collection에 반영
  - ex. HTMLCollection, NodeList
- Static Collection (non-live)
  - DOM이 변경되어도 collection 내용에는 영향을 주지 않음
  - `querySelectorAll()`의 반환 NodeList만 static collection

<br>

#### DOM - 변경 메서드

- `document.createElement()`
  - 작성한 태크명의 HTML 요소를 생성하여 반환
- `.append()`
  - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
  - 여러 개의 Node 객체, DOMString을 추가할 수 있음
  - 반환 값이 없음
- `appendChild()`
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능)
  - 한번에 오직 하나의 Node 추가 가능
  - 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동

##### append() vs. appendChild()

- `.append()` 를 사용하면 DOMString 객체를 추가할 수 있지만, `.appendChild()` 는 Node 객체만 허용
- `.append()`는 반환 겂이 없지만, `.appendChild()`는 추가된 Node 객체를 반환
- `.append()`는 여러 Node 객체와 문자열을 추가할 수 있지만, `.appendChild()`는 하나의 Node 객체만 추가할 수 있음

#### DOM - 변경 관련 속성

- `Node.innerText`
  - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text). 사람이 읽을 수 있는 요소만 남김
  - 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 스타일링이 적용된 모습으로 표현
- `Element.innerHTML`
  - 요소 내에 포함된 HTML 마크업을 반환
  - XSS 공격에 취약하므로 사용시 주의해야 함
    - 공격자가 웹사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법
    - 피해자(사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함 (CSRF 공격과 유사)

<br>

#### DOM - 삭제 메서드

- `.remove()`
  - Node가 속한 트리에서 해당 Node를 제거
- `.removeChild()`
  - DOM에서 자식 Node를 제거하고 제거된 Node를 반환
  - Node는 인자로 들어가는 자식 Node의 부모 Node

<br>

#### DOM - 속성 메서드

- `.setAttribute(name, value)`
  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름(name)과 값(value)으로 새로운 속성 추가
- `.getAttribute(attributeName)`
  - 해당 요소의 지정된 값(문자열)을 반환
  - 인자(attributeName)는 값을 얻고자 하는 속성의 이름

<br>

## Event Listener

### Event

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- 이벤트 발생
  - 마우스 클릭/키보드 누르기 등 사용자 행동으로 발생 가능
  - 특정 메서드(`Element.click()`)를 호출하여 프로그래밍적으로도 만들어 낼 수 있음

#### Event 기반 인터페이스

- AnimationEvent, ClipboardEvent, DragEvent 등
- UIEvent
  - 간단한 사용자 인터페이스 이벤트
  - Event의 상속을 받음
  - MouseEvent, KeyboardEvent, InputEvent, FocutEvent 등의 부모 객체 역할을 함

#### Event handler

- 대상에 특정 이벤트가 발생하면, 할일을 등록한다.

- `.addEventListener(type, listener[, options])`
  - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
  - 이벤트를 지원하는 모든 객체(Element, Document, Window 등)를 대상으로 지정 가능

- type
  - 반응할 이벤트 유형 (대소문자 구분 문자열)
- listener
  - 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
  - EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함

#### Event 취소

- `.preventDefault()`
  - 현재 이벤트의 기본 동작을 중단
  - 태그의 기본 동작을 작동하지 않게 막음
    - ex. a 태그의 기본동작은 클릭시 링크 이동. form 태그의 기본동작은 form 데이터 전송
  - 이벤트를 취소할 수 있는 경우, 이벤트 전파를 막지않고 그 이벤트를 취소

- 취소할 수 없는 이벤트도 존재함
  - 이벤트 취소 가능 여부는 `event.cancelable`을 사용해 확인할 수 있음