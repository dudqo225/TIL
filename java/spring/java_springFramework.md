# JAVA | Spring Framework

### 목차

> 1. Spring Framework

<br>

***

### 1. Spring Framework

#### 스프링 프레임워크

- 자바 플랫폼을 위한 오픈소스 애플리케이션 프레임워크
- 대규모 데이터 처리와 트랜잭션이 동시에 여러 사용자로부터 행해지는 매우 큰 규모의 환경, 엔터프라이즈 환경급 개발을 위한 솔루션
- IoC 기반의 프레임워크

<br>

#### IoC

- Inversion of Control. 제어의 역전
- 기존에는 프로그래밍을 하는 개발자들이 프로그램을 제어
  - 객체 결정 및 생성 → 의존성 객체 생성 → 객체 내의 메소드 호출 
- IoC는 프로그램에 대한 제어권을 제3자에게 위임하는 것
  - 객체의 생성부터 생명주기 등 모든 객체에 대한 제어권이 넘어간 것

<br>

##### IoC의 구성요소

- **DL**
  - Dependency Lookup. 의존성 검색
  - 컨테이너에서는 객체 관리를 위해 별도의 저장소에 빈(Bean)을 저장한다.
  - 컨테이너에서 제공하는 API를 이용하여 저장소에 저장되어 있는 빈을 검색하는 방법
- **DI**
  - Dependency Injection. 의존성 주입
  - 객체가 서로 의존하는 관계가 되도록 의존성을 주입하는 것
    - 의존성이란? 하나의 객체가 어떠한 다른 객체를 사용하고 있음을 의미
  - 각 클래스 사이에 필요로 하는 의존관계를 빈(Bean) 설정 정보를 바탕으로 하여 컨테이너가 자동으로 연결해준다.

<br>

#### POJO

- Plain Old Java Object. 평범한 자바 객체
- 이전의 Enterprise JavaBeans(EJB)는 확장 및 재사용이 가능한 로직을 개발하기 위해 사용됨

#### 

자바 if, for while 기초 알고리즘 코드 작성

입출력









### 참고 자료

[Spring Framework란?](https://khj93.tistory.com/entry/Spring-Spring-Framework%EB%9E%80-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90-%ED%95%B5%EC%8B%AC-%EC%A0%95%EB%A6%AC)

[IoC란 무엇인가](https://velog.io/@jeong-god/IoC%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80)

[Bean과 의존성 주입](https://ch4njun.tistory.com/219)

[인프런 - 스프링 입문](https://www.inflearn.com/course/spring_revised_edition#curriculum)