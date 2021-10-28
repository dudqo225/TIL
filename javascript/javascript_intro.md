# JavaScript | Intro

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



p.49 부터 정리!