# JAVA | RESTful  웹 서비스 구축

자바 스프링 프레임워크를 활용하여 RESTful 웹 서비스를 구축하는 연습을 해보자

본 문서에는 웹 애플리케이션의 전반적인 구조와 세부 개념들에 대해서 정리한다.

<br>

### 애플리케이션 구조

![image-20220111113140637](C:\Users\YB\AppData\Roaming\Typora\typora-user-images\image-20220111113140637.png)

- 표현 계층 (Presentation Layer)
  - Controller
  - View
- 비즈니스 계층 (Business Layer)
  - Service
- 영속성 계층 (Persistence Layer)
  - DAO (Data Access Object)

<br>

### 영속성 계층 (Persistence Layer)

영속성이란? 애플리케이션의 생명주기를 연장해주는 데이터의 속성. 애플리케이션이 실행을 멈춘 후에도 데이터를 사용할 수 있게 해줌

영속성을 이루는 방법에는 여러가지가 있다. 대표적으로 대용량 데이터 저장소를 제공하는 **데이터베이스(DB)**를 활용한다.



#### DAO (Data Access Object)

자바에서는 JDBC를 이용하여 DB에 접속, 데이터 접근이 가능하다. 좀 더 편리하게 퍼시스턴스 계층을 구현하기 위해 **ORM(Object-Relational Mapping), 퍼시스턴스 프레임워크**를 사용하면 좋다.

Connection 생성, Statement 생성, ResultSet 처리, SQLException 처리 같은 반복작업을 대신 처리함으로써 편리성이 향상된다.

##### ORM, 퍼시스턴스 프레임워크

Hibernate, Mybatis, JPA(Java Persistence API), JDO(Java Data Objects) 등이 있음

장점

- 생산성 향상
- SQL 작성 → 객체 생성 등의 번거로운 작업을 대신해줌
- 유지보수가 쉽다

단점

- 초반에 배울 때 어렵다
- 객체지향적으로 클래스 설계가 쉽지 않음
- 잘못 사용하면 성능 저하 발생

<br>

그렇다면, **DAO** 란? → **퍼시스턴스 계층을 구현하는 자바 클래스**

- MyBatis : Mapper
- JPA : Repository

라고 부른다.

