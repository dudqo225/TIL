# JAVA | Generic

### 목차

>1. 제네릭
>2. 제네릭을 사용하는 이유
>
>

<br>

***

### 1. 제네릭

#### 제네릭(Generic)이란?

- 클래스 내부에서 사용할 데이터 타입을 외부에서 지정하는 기법
- 클래스를 정의할 때 변수의 데이터 타입을 확정하지 않고, 인스턴스를 생성할 때 데이터 타입을 지정하는 기능

```java
// 제네릭 예제
class Person<T> {
    public T info;
}

public class GenericDemo {
    public static void main(String[] args) {
        Person<String> p1 = new Person<String>();
        Person<StringBuilder> p2 = new Person<StringBuilder>();
    }
}
```

- `p1` 의 데이터 타입은 String, `p2`의 데이터 타입은 StringBuilder 이다.

<br>

***

### 2. 제네릭을 사용하는 이유

#### 타입 안전성

```java
class StudentInfo{
    public int grade;
    StudentInfo(int grade){ this.grade = grade; }
}
class EmployeeInfo{
    public int rank;
    EmployeeInfo(int rank){ this.rank = rank; }
}

class Person{
    public Object info;
    Person(Object info){ this.info = info; }
}

public class GenericDemo {
    public static void main(String[] args) {
        Person p1 = new Person("부장");
        EmployeeInfo ei = (EmployeeInfo)p1.info;
        System.out.println(ei.rank);
    }
}
```

- Person의 생성자의 매개변수 infor의 데이터 타입이 `Object` 이다.
- 모든 객체가 될 수 있기 때문에 EmployeeInfo가 아닌 String이 와도 컴파일 에러가 발생하지 않는다.
- 하지만 런타임 에러가 발생한다.
  - 실제 애플리케이션이 동작하고 있는 상황에서 발생하기 때문에 런타임 에러는 심각한 문제를 초래할 수 있음
- 이러한 에러를 타입에 대해서 안전하지 않다고 함.
- 모든 타입이 올 수 있기 때문에 타입을 엄격하게 제한할 수 없는 것임

<br>

#### 제네릭화

- 위 문제를 제네릭화하여 해결해보자

```java
class StudentInfo{
    public int grade;
    StudentInfo(int grade){ this.grade = grade; }
}
class EmployeeInfo{
    public int rank;
    EmployeeInfo(int rank){ this.rank = rank; }
}

class Person<T>{
    public T info;
    Person(T info){ this.info = info; }
}

public class GenericDemo {
    public static void main(String[] args) {
        Person<EmployeeInfo> p1 = new Person<EmployeeInfo>(new EmployeeInfo(1));
        EmployeeInfo ei1 = p1.info;
        System.out.println(ei1.rank); // 성공
         
        Person<String> p2 = new Person<String>("부장");
        String ei2 = p2.info;
        System.out.println(ei2.rank); // 컴파일 실패
    }
}
```

- int 대신 String을 호출하기 때문에 컴파일 실패
  - 컴파일 단계에서 오류 검출
  - 중복 제거 및 타입 안전성을 동시에 추구할 수 있음

<br>

***

### 3. 제네릭의 특성

#### 복수의 제네릭

- 클래스 내에서 여러개의 제네릭 사용 가능

```java
class EmployeeInfo{
    public int rank;
    EmployeeInfo(int rank){ this.rank = rank; }
}

class Person<T, S>{
    public T info;
    public S id;
    Person(T info, S id){ 
        this.info = info; 
        this.id = id;
    }
}

public class GenericDemo {
    public static void main(String[] args) {
        Person<EmployeeInfo, int> p1 = new Person<EmployeeInfo, int>(new EmployeeInfo(1), 1);
    }
}
```

- 위 코드는 예외를 발생시키는 한다.

<br>

#### 기본 데이터 타입과 제네릭

- 제네릭은 참조 데이터 타입에 대해서만 사용 가능
- 기본 데이터 타입에서는 사용할 수 없음

```java
// 위 코드 오류 해결
class EmployeeInfo{
    public int rank;
    EmployeeInfo(int rank){ this.rank = rank; }
}

class Person<T, S>{
    public T info;
    public S id;
    Person(T info, S id){ 
        this.info = info;
        this.id = id;
    }
}

public class GenericDemo {
    public static void main(String[] args) {
        EmployeeInfo e = new EmployeeInfo(1);
        Integer i = new Integer(10);
        Person<EmployeeInfo, Integer> p1 = new Person<EmployeeInfo, Integer>(e, i);
        System.out.println(p1.id.intValue());
    }
}
```

##### Integer

- `new Integer` 는 기본 데이터 타입 int 를 참조 데이터 타입으로 변환해주는 역할을 함
- 이러한 클래스를 **wrapper** 클래스라고 함

<br>

#### 제네릭의 생략

- 제네릭은 생략 가능함

```java
// p1과 p2 코드는 동일하게 동작함
EmployeeInfo e = new EmployeeInfo(1);
Integer i = new Integer(10);

Person<EmployeeInfo, Integer> p1 = new Person<EmployeeInfo, Integer>(e, i);
Person p2 = new Person(e, i);
```

<br>

#### 메소드에 적용

- 제네릭은 메소드에 적용할 수 있음

```java
class EmployeeInfo{
    public int rank;
    EmployeeInfo(int rank){ this.rank = rank; }
}
class Person<T, S>{
    public T info;
    public S id;
    Person(T info, S id){ 
        this.info = info;
        this.id = id;
    }
    
    public <U> void printInfo(U info){
        System.out.println(info);
    }
}

public class GenericDemo {
    public static void main(String[] args) {
        EmployeeInfo e = new EmployeeInfo(1);
        Integer i = new Integer(10);
        Person<EmployeeInfo, Integer> p1 = new Person<EmployeeInfo, Integer>(e, i);
        // 아래 두줄의 코드는 동일함
        p1.<EmployeeInfo>printInfo(e);
        p1.printInfo(e);
    }
}
```

<br>

#### 제네릭의 제한

##### extends

- 제네릭으로 올 수 있는 데이터 타입을 특정 클래스의 자식으로 제한할 수 있음

```java
abstract class Info{
    public abstract int getLevel();
}
class EmployeeInfo extends Info{
    public int rank;
    EmployeeInfo(int rank){ this.rank = rank; }
    public int getLevel(){
        return this.rank;
    }
}
class Person<T extends Info>{
    public T info;
    Person(T info){ this.info = info; }
}
public class GenericDemo {
    public static void main(String[] args) {
        Person p1 = new Person(new EmployeeInfo(1));
        // Info의 자식이 아니기 때문에 오류 발생
        Person<String> p2 = new Person<String>("부장");
    }
}
```

- 구현(implements) 관계에서도 사용 가능 - Interface

<br>

***

### 4.참고 자료

[생활코딩 - JAVA - Generic](https://opentutorials.org/course/1223/6237)