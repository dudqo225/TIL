# JavaScript | Vuex

### 목차

> Vuex
>
> Vuex Core Concepts
>
> Todo app with Vuex

<br>

## Vuex

### Vuex

- 상태 관리 패턴 + 라이브러리 (Statement management pattern + Library)
- 상태 (state)를 전역 저장소로 관리할 수 있도록 지원하는 라이브러리
  - 상태가 예측가능한 방식으로만 변경될 수 있도록 보장하는 규칙을 설정
  - **중앙 집중식 저장소** 역할

#### State

- Data
- 해당 애플리케이션의 핵심이 되는 요소
- 중앙에서 관리하는 모든 상태 정보

#### 상태 관리 패턴

- 컴포넌트의 공유된 상태를 추출하고 이를 전역에서 관리하도록 함
- 컴포넌트는 커다란 view가 되고 모든 컴포넌트는 트리 구조에 상관없이 상태에 엑세스하거나 동작을 트리거할 수 있음
- 상태 관리 및 특정 규칙 적용과 관련된 개념을 정의하고 분리함으로써 **코드의 구조와 유지 관리 기능 향상**

#### 기존 Pass props & Emit event

- 단방향 데이터 흐름

  - state는 앱을 작동하는 원본 소스 (data)
  - view는 state의 선언적 매핑
  - action은 view에서 사용자 입력에 대해 반응적으로 state를 바꾸는 방법 (methods)

  ![image-20211114173220914](javascript_vuex.assets/image-20211114173220914.png)

#### Vuex를 활용한 state 관리

- 상태를 한 곳(store)에 모아 놓고 관리 가능
- 상태의 변화는 모든 컴포넌트에서 공유
- 상태 변화는 오로지 Vuex가 관리하고 해당 상태를 공유하고 있는 모든 컴포넌트는 state의 변화에 반응

![image-20211114173352228](javascript_vuex.assets/image-20211114173352228.png)

<br>

## Vuex Core Concepts







## Todo app with Vuex