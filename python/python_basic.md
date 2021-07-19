## Python_basic



### 특징

- 인터프리터 언어 : 컴파일 언어에 비해 다소 느리지만, 한 줄씩 코드를 읽으면서 실행
- 객체 지향 프로그래밍(OOP)
- 동적 타이핑 (Dynamic Typing) : 변수에 별도의 타입을 지정할 필요가 없다.



### 코드 스타일 가이드

- PEP 8 : 파이썬의 기본 스타일 가이드
- Google Python Style Guide

> 기본 스타일을 지키지 않으면, 남들이 보기 싫은 코드가 된다!!!





##### overflow (오버플로) : 데이터 타입별 사용 가능한 메모리 크기를 넘는 상황

- python에서는 오버플로 현상이 발생하지 않음.
- Arbitrary precision arithmetic(임의 정밀도 산술)을 통해 가용 메모리를 활용하여 모든 수를 표현



##### Boolean

- `0`, `0.0`, `()`, `{}`, `[]`, `''`, `None`  : 6가지는 모두 False를 반환





### 타입 변환

1. 암묵적(암시적) 타입 변환_Implicit : 파이썬 내부적으로 타입 변환
2. 명시적 타입 변환_Explicit : 사용자가 특정함수를 통해 의도적으로 타입을 변환



### 연산자

1. 산술
2. 비교
3. 논리
4. 복합
5. 기타 - concatenation, containment, identity, indexing & slicing



### 표현식 & 문장

문장(statement)이 표현식(expression)보다 큰 개념

- 표현식 : 식별자, 값, 연산자로 구성. 하나의 값으로 환원(reduce)될 수 있는 문장
- 문장 : 파이썬이 실행가능한 최소한의 코드 단위
  - 모든 표현식은 문장이다.





