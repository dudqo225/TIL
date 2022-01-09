# JAVA | OOP

### 목차

> 1. 객체지향 프로그래밍
> 2. 메소드화
> 3. 객체화
> 4. 멤버
> 5. 초기화와 생성자
> 6. 참고 자료

<br>

### 1.객체지향 프로그래밍

- Object-Oriented Programming (OOP)
- 로직을 상태(state)와 행위(behave)로 이루어진 객체로 만드는 것
- 객체들을 레고 블럭처럼 조립하여 하나의 프로그램을 만드는 것

<br>

#### 부품화

- ex. 컴퓨터
  - 초창기 컴퓨터는 본체 - 모니터 - 키보드가 하나로 단일화되어 있음. 만약 모니터가 고장나면 컴퓨터 전체를 바꿔야 하고, 키보드가 고장나도 컴퓨터를 바꿔야 함
  - 최근의 컴퓨터는 모니터 - 본체 - 키보드가 분리되어 있음. 즉, 부품화 시킨 것. 기능들을 부품화, 세분화 시킴으로써 소비자들이 더 좋은 키보드 or 가성비 좋은 모니터를 선택할 수 있음. 또, 문제 발생시 원인을 파악하고 해당 부품만 고쳐서 문제 해결하기 쉬움
- OOP
  - 메소드를 활용하여 코드의 양을 줄이고, 기능별로 메소드를 분류
  - 필요한 코드를 빨리 찾을 수 있고 문제 진단도 빨라짐
  - **메소드와 메소드가 사용하는 변수들을 분류하고 그룸핑하는 것 → 객체(Object)**

<br>

#### 은닉화, 캡슐화

- 부품이 어떻게 만들어졌는지 모르는 사람도 부품을 사용하는 방법만 알면 쓸 수 있는 것
- 정보의 은닉화(Information Hiding), 캡슐화(Encapsulation)

<br>

#### 인터페이스

- Interface
- 모니터 > 컴퓨터가 어떻게 만들어졌는지 중요하지 않음. 컴퓨터 > 모니터가 어떻게 만들어졌는지 중요하지 X
  - HDMI 케이블(연결점)의 모양을 각 표준에 맞게 만들면 됨
  - 즉, 인터페이스는 부품들 간의 약속



***

### 2. 메소드화

- 숫자 더하기 코드 예시

```java
public class CalculatorDemo {
 
    public static void main(String[] args) {
        // 아래의 로직이 1000줄 짜리의 복잡한 로직이라고 가정하자.
        System.out.println(10 + 20);
        System.out.println(20 + 40);
    }
 
}
```

- 코드의 양을 줄이고, 문제 발생시 원인을 쉽게 찾기 위해 로직을 메소드로 만들어 보자

```java
public class CalculatorDemo2 {
 
    public static void sum(int left, int right) {
        System.out.println(left + right);
    }
 
    public static void main(String[] args) {
        sum(10, 20);
        sum(20, 40);
    }
 
}
```

- 더하기 외에 평균을 구하고자 하면?

```java
public class CalculatorDemo3 {
    
    public static void avg(int left, int right) {
        System.out.printIn((left + right) / 2);
    }
    
    public static void sum(int left, int right) {
        system.out.printIn(left + right);
    }
    
    public static void main(String[] args) {
        int left, right;
        
        left = 10;
        right = 20;
        
        sum(left, right);
        avg(left, right);
        
        left = 20;
        right = 40;
        
        sum(left, right);
        avg(left, right);s
    }
}
```

- 점점 코드가 복잡해지면서 버그가 많아질 수 밖에 없다. 객체 지향적으로 설계를 해서 문제를 해결하고 상황을 완화할 필요가 있음



***

### 3 . 객체화

- 의미적으로 연관된 로직들을 물리적으로 응집된 하나의 객체로 만드는 것
- 재활용성을 높일 수 있음

```java
// 계산기 예시

package org.opentutorials.javatutorials.object;

class Calculator{
    int left, right;
    
    public void setOprands(int left, int right) {
        this.left = left;
        this.right = right;
    }
    
    public void sum() {
        System.out.printIn(this.left + this.right);
    }
    
    public void avg() {
        System.out.printIn((this.left + this.right) / 2);
    }
}

public class CalculatorDemo4 {
    public static void main(String[] args) {
        
        Calculator c1 = new Calculator();
        c1.setOprands(10, 20);
        c1.sum();
        c1.avg();
        
        Calculator c2 = new Calculator();
        c2.setOprands(20, 40);
        c2.sum();
        c2.avg();
    }
}
```

<br>

#### 클래스

- `class Calculator {}`
- 클래스란? 연관되어 있는 변수와 메소드의 집합
- 일종의 **설계도**

<br>

#### 인스턴스

- `Calculator c1 = new Calculator();`
- 설계도를 구체적인 **제품**으로 만드는 것. `new` 키워드 사용
- **Instance**
- 클래스를 인스턴스화 할때는 변수에 담아야 하고, 사용하는 변수의 데이터 타입은 해당 클래스가 된다.

<br>

##### this.

- 클래스를 통해서 만들어진 인스턴스 자신을 가리킴
- 메소드 밖에서 선언한 변수는 인스턴스 내의 모든 메소드에서 접근 가능

<br>

- 변수 ≒ 상태(state)
- 메소드 ≒ 행동(behave)

- 하나의 클래스를 바탕으로 서로 다른 상태를 가진 인스턴스를 만들면 서로 다른 행동을 하게 된다!

<br>



***

### 4. 멤버

- 객체의 멤버(구성)
  - 변수
  - 메소드

<br>

#### 클래스 변수

- 경우에 따라서 모든 인스턴스가 같은 값을 공유하게 하고 싶을 수 있다
  - 각각의 인스턴스마다 별도의 값을 가지고 있을 필요가 없을 때
  - 변수를 클래스의 멤버로 만들면 된다

```java
// 클래스 변수 예시

class Calculator {
    static double PI = 3.14;
    int left, right;
 
    public void setOprands(int left, int right) {
        this.left = left;
        this.right = right;
    }
 
    public void sum() {
        System.out.println(this.left + this.right);
    }
 
    public void avg() {
        System.out.println((this.left + this.right) / 2);
    }
}
 
public class CalculatorDemo1 {
 
    public static void main(String[] args) {
 
        Calculator c1 = new Calculator();
        System.out.println(c1.PI);
 
        Calculator c2 = new Calculator();
        System.out.println(c2.PI);
 
        System.out.println(Calculator.PI);
 
    }
 
}
```

- **`static` 을 변수나 메소드 앞에 붙이면 클래스의 멤버가 된다.**
- 클래스 변수에 접근하는 방법
  - 인스턴스를 통해 접근
    - `c1.PI`
  - 클래스를 통해서 접근
    - `Calculator.PI`
- 변수의 변경사항을 모든 인스턴스에서 공유해야 할 때

```java
class Calculator2 {
    static double PI = 3.14;
    // 클래스 변수인 base가 추가되었다.
    static int base = 0;
    int left, right;
 
    public void setOprands(int left, int right) {
        this.left = left;
        this.right = right;
    }
 
    public void sum() {
        // 더하기에 base의 값을 포함시킨다.
        System.out.println(this.left + this.right + base);
    }
 
    public void avg() {
        // 평균치에 base의 값을 포함시킨다.
        System.out.println((this.left + this.right + base) / 2);
    }
}
 
public class CalculatorDemo2 {
 
    public static void main(String[] args) {
 
        Calculator2 c1 = new Calculator2();
        c1.setOprands(10, 20);
        // 30 출력
        c1.sum();
 
        Calculator2 c2 = new Calculator2();
        c2.setOprands(20, 40);
        // 60 출력
        c2.sum();
 
        // 클래스 변수 base의 값을 10으로 지정했다.
        Calculator2.base = 10;
 
        // 40 출력
        c1.sum();
 
        // 70 출력
        c2.sum();
 
    }
 
}
```

<br>

- 클래스 변수의 용도
  - 인스턴스에 따라서 변하지 않는 값이 필요한 경우
    - `final` 로 상수 선언하는 것이 바람직
  - 인스턴스를 생성할 필요가 없는 값을 클래스에 저장하고 싶은 경우
  - 값의 변경 사항을 모든 인스턴스가 공유해야 하는 경우

<br>

#### 클래스 메소드

- 인스턴스가 굳이 변수를 유지하고 있을 필요가 없을 때가 있다

```java
// 계산기 클래스의 예시

class Calculator3{
  
    public static void sum(int left, int right){
        System.out.println(left+right);
    }
     
    public static void avg(int left, int right){
        System.out.println((left+right)/2);
    }
}
 
public class CalculatorDemo3 {
     
    public static void main(String[] args) {
        Calculator3.sum(10, 20);
        Calculator3.avg(10, 20);
         
        Calculator3.sum(20, 40);
        Calculator3.avg(20, 40);
    }
 
}
```

- 메소드가 인스턴스 변수를 참조하지 않는다면 클래스 메소드를 사용해서 불필요한 인스턴스의 생성을 막을 수 있음



##### 클래스와 인스턴스의 차이

1. 인스턴스 메소드는 클래스 멤버에 접근 할 수 있다 ⭕
2. 클래스 메소드는 인스턴스 멤버에 접근 할 수 없다 ❌
   - 인스턴스 변수는 인스턴스가 만들어지면서 생성되고, 클래스 메소드는 인스턴스가 생성되기 전에 만들어진다. 따라서 먼저 만들어진 클래스 메소드가 인스턴스 멤버에 접근할 수 없다.

```java
class C1{
    static int static_variable = 1;
    int instance_variable = 2;
   
    static void static_static(){
        System.out.println(static_variable);
    }
    
    static void static_instance(){
        // 클래스 메소드에서는 인스턴스 변수에 접근 할 수 없다. 
        //System.out.println(instance_variable);
    }
    
    void instance_static(){
        // 인스턴스 메소드에서는 클래스 변수에 접근 할 수 있다.
        System.out.println(static_variable);
    }
    
    void instance_instance(){        
        System.out.println(instance_variable);
    }
}
public class ClassMemberDemo {  
    public static void main(String[] args) {
        C1 c = new C1();
        
        // 인스턴스를 이용해서 정적 메소드에 접근 -> 성공
        // 인스턴스 메소드가 정적 변수에 접근 -> 성공
        c.static_static();
        
        // 인스턴스를 이용해서 정적 메소드에 접근 -> 성공
        // 정적 메소드가 인스턴스 변수에 접근 -> 실패
        c.static_instance();
        
        // 인스턴스를 이용해서 인스턴스 메소드에 접근 -> 성공
        // 인스턴스 메소드가 클래스 변수에 접근 -> 성공
        c.instance_static();
        
        // 인스턴스를 이용해서 인스턴스 메소드에 접근 -> 성공 
        // 인스턴스 메소드가 인스턴스 변수에 접근 -> 성공
        c.instance_instance();
        
        // 클래스를 이용해서 클래스 메소드에 접근 -> 성공
        // 클래스 메소드가 클래스 변수에 접근 -> 성공
        C1.static_static();
        
        // 클래스를 이용해서 클래스 메소드에 접근 -> 성공
        // 클래스 메소드가 인스턴스 변수에 접근 -> 실패
        C1.static_instance();
        
        // 클래스를 이용해서 인스턴스 메소드에 접근 -> 실패
        //C1.instance_static();
        
        // 클래스를 이용해서 인스턴스 메소드에 접근 -> 실패
        //C1.instance_instance();
    }
 
}
```

<br>

##### 용어

- 인스턴스 변수 → Non-Static Field
- 클래스 변수 → Static Field
- 필드(Field)란 클래스 전역에서 접근할 수 있는 변수를 의미함



***

### 5. 초기화와 생성자

#### 초기화

- 어떤 일을 시작하기 전에 준비를 하는 것
- **생성자(constructor)**

```java
// 계산기 예제의 초기화
Calculator c1 = new Calculator();
c1.setOprands(10, 20);
c1.sum();
c1.avg();
```

- `c1.setOprands(10, 20)` 처럼 인스턴스 변수를 설정하는 메소드를 호출하지 않는다면?

```java
c1.sum();
c1.avg();
```

- 위 2 개의 메소드를 호출해도 원하는 결과를 얻을 수 없음

- 객체 Calculator를 사용하기 위해 반드시 `setOprands` 를 호출해야 함
  - 절차를 기억해야 하기 때문에 사용자 입장에서 불편하고,
  - 잘못된 사용으로 오류가 발생할 확률이 높아진다.

<br>

#### 생성자

- 인스턴스가 생성될 때, left / right 변수 값을 입력하도록 강제한다면?

```java
class Calculator {
    int left, right;
 
    public Calculator(int left, int right) {
        this.left = left;
        this.right = right;
    }
 
    public void sum() {
        System.out.println(this.left + this.right);
    }
 
    public void avg() {
        System.out.println((this.left + this.right) / 2);
    }
}
 
public class CalculatorDemo1 {
 
    public static void main(String[] args) {
 
        Calculator c1 = new Calculator(10, 20);
        c1.sum();
        c1.avg();
 
        Calculator c2 = new Calculator(20, 40);
        c2.sum();
        c2.avg();
    }
 
}
```

- 절차를 하나 줄이고 객체 생성시 left / right 변수 값을 설정하는 과정을 강제

##### 생성자의 특징

1. 값을 반환하지 않음
   - 생성자는 인스턴스를 생성해주는 역할을 하는 특수한 메소드
   - 반환값을 필요로하는 작업에서는 생성자를 사용하지 X
   - return이 없고, 반환값을 메소드 정의에 포함시키지도않음
2. 생성자 이름 == 클래스 이름
   - 자바에서 클래스 이름과 생성자 메소드 이름을 동일하게 적용하는 것이 약속임



***

### 참고 자료

[생활코드 - JAVA | 객체지향 프로그래밍](https://opentutorials.org/course/1223/5399)