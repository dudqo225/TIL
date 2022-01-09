# JAVA | Advanced

### 목차

>1. abstract
>2. final
>3. 인터페이스
>4. 다형성
>5. 참고 자료

<br>

***

### 1. abstract

- 추상
- 상속을 강제하는 일종의 규제
- abstract 클래스나 메소드를 사용하기 위해서는 반드시 상속해서 사용하도록 강제하는 것

<br>

#### 추상 메소드

- 메소드의 시그니처만 정의된 비어있는 메소드

```java
// 추상 메소드 예시
abstract class A {
    // 본체가 비어 있는 메소드
    public abstract int b();
    
    // 본체가 있는 메소드는 abstract 키워드를 가질 수 없음
    // public abstract int c() { System.out.printIn("Hello") };
    
    // 추상 메소드가 아닌 메소드 존재 가능
    public void d() {
        System.out.printIn("World");
    }
}

public class AbstractDemo {
    public static void main(String[] args) {
        // 추상 클래스 A를 인스턴스화 하는 코드이지만 오류가 발생한다.
        A obj = new A();
    }
}
```

- 추상 클래스 A를 인스턴스화할 때 오류가 발생하는데, 이는 구체적인 메소드 내용이 존재하지 않기 때문에 인스턴스화시켜서 사용할 수 없는 것임

<br>

#### 추상 클래스의 상속

- 위 문제를 해결하기 위해서 클래스 A를 상속한 하위 클래스를 만들고, 추상 메소드를 오버라이드 해서 내용이 있는 메소드를 만들어야 함
  - 클래스 A를 상속하는 클래스 B를 생성
  - 클래스 A의 추상 메소드인 메소드 `b` 를 오버라이딩 한다

```java
abstract class A {
    public abstract int b();
    public void d() {
        System.out.printIn("World");
    }
}

class B extends A {
    public int b() {return 1;}
}

public class AbstractDemo {
    public static void main(String[] args) {
        B obj = new B();
        System.out.printIn(obj.b());
    }
}
```

<br>

#### 추상 클래스 사용 이유

- 추상이란?
  - 부모 클래스에 메소드의 시그니처만 정의하고, 메소드의 실제 동작 방법은 메소드를 상속 받은 하위 클래스의 책임으로 위임하는 것

- 상황에 따라 동작 방법이 달라지는 메소드는 추상 메소드로 만들어서 하위 클래스에서 구현하도록 하고,
- 모든 클래스의 공통분모 메소드는 상위 클래스에 두어서 **코드의 중복, 유지보수의 편의성**을 꾀할 수 있음

<br>

#### 디자인 패턴

- Design Pattern
- 좋은 소프트웨어를 만들기 위한 설계
- 장점
  - 좋은 설계를 단기간에 학습할 수 있음
  - 소통에 도움이 됨

<br>

***

### 2. final

- abstract의 반대 개념
- 상속/변경을 금지하는 규제

<br>

#### final 필드

- 필드 == 변수

- 실행되는 과정에서 한번 값이 정해진 이후로는 변수 내의 값이 바뀌지 않도록 하는 규제

```java
class Calculator {
    static final double PI = 3.14;
    int left, right;
    
    ...
}
```

- `PI`  앞에 final이 붙어 있으므로, 이 변수 값을 변경하려고 해도 자바는 허용하지 않는다

<br>

#### final 메소드

- final 필드(변수)만큼 사용 빈도가 높지는 않음

```java
class A {
    final void b() {}
}
class B extends A {
    void b() {}
}
```

- final 메소드 `b` 를 상속하려 하기 때문에 오류가 발생

<br>

#### final 클래스

- final 클래스를 상속하려 하면 오류가 발생

```java
final classs C {
    final void b() {}
}
class D extends C {}
```

<br>

***

### 3. 인터페이스

#### 인터페이스(interface)란?

- 어떤 객체가 있고 이 객체가 특정한 인터페이스를 사용한다면, 이 객체는 반드시 인터페이스의 메소드들을 구현해야 함
- 인터페이스에서 강제하고 있는 메소드를 구현하지 않으면 이 애플리케이션은 컴파일조차 되지 않음

```java
// 인터페이스 예제
interface I{
    public void z();
}

class A implements I{
    public void z() {}
}
```

- `class A implements I` 는 **클래스 A가 인터페이스 I를 구현**하고 있다는 의미임
- `I` 의 멤버인 `z()` 메소드를 클래스 A가 반드시 포함하고 있어야 함!
  - 포함하지 않으면 컴파일 에러가 발생

<br>

##### 상속 vs. 인터페이스

- 상속
  - 상위 클래스 기능을 하위 클래스가 물려 받는 것
  - `class` / `extends`
- 인터페이스
  - 하위 클래스에 특정 메소드가 반드시 존재하도록 강제
  - `interace` / `extends`

<br>

#### 인터페이스의 실질적인 쓰임

- 예시
  - 계산기 기능 관련 프로젝트를 진행하려 함
  - 계산기 클래스는 개발자 A가 만들고, 개발자 B는 이 클래스를 사용하는 로직을 만든다
  - 코드를 합쳐보니 개발자 A는 매개변수를 2개 받는 클래스를 생성. 개발자 B는 매개변수가 3개일 것이라 예상하고 코드를 작성함. 문제가 발생했다..!!
  - 문제 해결을 위해 협업자 상호간 구체적인 약속을 하자 → **인터페이스**

```java
// 인터페이스 생성
public interface Calculatable {
    public void setOprands(int first, int second, int third);
    public int sum();
    public int avg();
}
```

- 위 인터페이스를 활용하여 개발자 A는 클래스를 구현
- 위 인터페이스를 활용하여 개발자 B는 가짜 클래스를 임시로 구현하여 애플리케이션을 생성
- 개발자 B가 구현한 가짜 클래스를 개발자 A가 구현한 실제 로직으로 교체

<br>

#### 인터페이스의 규칙

- 하나의 클래스가 여러개의 인터페이스를 구현할 수 있다.
- 인터페이스도 상속이 된다.
- 인터페이스의 멤버는 반드시 `public` 이다.

<br>

##### abstract vs. interface

- abstract
  - 일반적인 클래스
  - 구체적인 로직이나 상태를 가지고 있을 수 있음
- interface
  - 클래스가 아닌 인터페이스라는 고유한 형태를 가지고 있음
  - 구체적인 로직이나 상태를 가지고 있을 수 없음

<br>

***

### 4. 다형성

#### 다형성 (Polymorphism)

- 하나의 메소드나 클래스가 있을 때 이것들이 다양한 방법으로 동작하는 것을 의미함
- ex.
  - 키보드의 키 : "누른다"
  - ESC → 취소 | ENTER → 실행
- 동일한 조작방법으로 동작하지만 동작 방법이 다른 것

<br>

#### overloading과 다형성

```java
// 예제
class O {
    public void a(int param) {
        System.out.printIn("숫자출력");
        System.out.printIn(param);
    }
    public void a(String param) {
        System.out.printIn("문자출력");
        System.out.printIn(param);
    }
}
public class PolymorphismOverloadingDemo {
    public static void main(String[] args) {
        O o = mew O();
        o.a(1);
        o.a("one");
    }
}
```

- 클래스 O의 메소드 a는 두 개의 본체를 가지고 있다. 동시에 하나의 이름인 a를 공유하고 있다.
- 이름이 같지만 서로 다른 동작 방법을 가지고 있음.

<br>

#### 클래스와 다형성

- 클래스 B가 클래스 A를 상속할 때 클래스 B는 클래스 A를 데이터 형으로 삼을 수 있음

```java
// 예시
class A{
    public String x(){return "A.x";}
}
class B extends A{
    public String x(){return "B.x";}
    public String y(){return "y";}
}
public class PolymorphismDemo1 {
    public static void main(String[] args) {
        A obj = new B();
        System.out.println(obj.x());
    }
}
```

```java
// 결과
B.x
```

- class `B` 의 데이터 타입을 `A`로 했을 때, `B`의 메소드 `y` 가 존재하지 않는 것처럼 실행되지 않음
  - 클래스 B가 클래스 A화 되었다.
- class` B`의 데이터 타입을 `A`로 했을 때, `B`의 메소드 `x`를 실행하면 클래스 `A`가 아닌 `B`에서 정의된 메소드가 실행됨
  - 클래스 B의 기본적인 성질은 그대로 간직함
- 클래스 B를 클래스 A의 데이터 타입으로 인스턴스화 했을 때 클래스 A에 존재하는 멤버만이 클래스 B의 멤버가 됨. 동시에 클래스 B에서 오버라이딩한 멤버의 동작방식은 그대로 유지한다.

<br>

#### 인터페이스와 다형성

- 주석처리된 코드는 오류가 발생함 각 obj, objI2, objI3의 데이터 타입이 다르기 때문

```java
interface I2{
    public String A();
}
interface I3{
    public String B();
}
class D implements I2, I3{
    public String A(){
        return "A";
    }
    public String B(){
        return "B";
    }
}
public class PolymorphismDemo3 {
    public static void main(String[] args) {
        D obj = new D();
        I2 objI2 = new D();
        I3 objI3 = new D();
         
        obj.A();
        obj.B();
         
        objI2.A();
        //objI2.B();
         
        //objI3.A();
        objI3.B();
    }
}
```

<br>

#### 비유

- 직장에서는 인터페이스인 `programmer`가 중요함.
- 두 사람의 종교, 가족관계는 상관없이 `programmer`라는 인터페이스를 가지고 있으면 고용할 수 있다.
- `programmer` 인터페이스는 `coding` 이라는 메소드를 구현하고 있다.
- 두 사람에게 업무요청을 하면 `programmer` 인터페이스의 메소드 `coding`을 통해 요청하면 되는데, 이때 두 사람 각각의 성향/능력에 따라서 수행 결과가 다르다.

```java
interface father{}
interface mother{}
interface programmer{
    public void coding();
}
interface believer{}
class Steve implements father, programmer, believer{
    public void coding(){
        System.out.println("fast");
    }
}
class Rachel implements mother, programmer{
    public void coding(){
        System.out.println("elegance");
    }
}
public class Workspace{
    public static void main(String[] args){
        programmer employee1 = new Steve();
        programmer employee2 = new Rachel();
         
        employee1.coding();
        employee2.coding();
    }
}
```

<br>

***

### 5. 참고 자료

[생활코딩 - JAVA](https://opentutorials.org/course/1223/6127)

