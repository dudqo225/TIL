# JAVA | OOP Ⅱ

### 목차

>1. 상속
>
>2. 상속과 생성자
>
>3. overriding
>4. overloading
>5. 참고 자료

<br>

### 1. 상속

#### 상속이란?

- 상속. Inheritance
- 객체지향의 재활용성을 극대화시킨 프로그래밍 기법
- 어떤 객체의 필드(변수)와 메소드를 다른 객체가 물려 받는 기능
- 기존 객체를 수정하지 않으면서 새로운 객체가 기존 객체를 기반으로 만들어지게 되는 것
- 부모 - 자식 | 상위(super) - 하위(sub) | 기초(base) - 유도(derived)

```java
// 계산기 예제
package org.opentutorials.javatutorials.Inheritance.example1;
 
class Calculator {
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
 
class SubstractionableCalculator extends Calculator {
    public void substract() {
        System.out.println(this.left - this.right);
    }
}
 
public class CalculatorDemo1 {
 
    public static void main(String[] args) {
 
        SubstractionableCalculator c1 = new SubstractionableCalculator();
        c1.setOprands(10, 20);
        c1.sum();
        c1.avg();
        c1.substract();
    }
 
}
```

- **`extends`** 키워드 사용



#### 상속의 장점 및 단점

##### 장점

- 코드의 중복을 제거
- 유지보수가 편리해짐
- 재활용성

##### 단점

- 복잡도의 증가

<br>

***

### 2. 상속과 생성자

- 클래스에 매개변수가 있는 생성자가 존재할 때에는 자동으로 기본 생성자를 만들어주지 않음

```java
// 오류 발생
public class ConstructorDemo {
    public ConstructorDemo(int param1) {}
    public static void main(String[] args) {
        ConstructorDemo  c = new ConstructorDemo();
    }
}
```

```java
// 기본 생성자 추가하여 오류 발생 x
public class ConstructorDemo {
    public ConstructorDemo(){}
    public ConstructorDemo(int param1) {}
    public static void main(String[] args) {
        ConstructorDemo  c = new ConstructorDemo();
    }
}
```



- 하위 클래스에서 상위 클래스를 상속받을 때
  - 메소드가 아닌 생성자를 통해서 변수 설정을 하고 싶다면

```java
class Calculator {
    int left, right;
    
    // 생성자 추가
    public Calculator(int left, int right){
        this.left = left;
        this.right = right;
    }
     
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
 
class SubstractionableCalculator extends Calculator {
    public SubstractionableCalculator(int left, int right) {
        this.left = left;
        this.right = right;
    }
 
    public void substract() {
        System.out.println(this.left - this.right);
    }
}
 
public class CalculatorConstructorDemo5 {
    public static void main(String[] args) {
        SubstractionableCalculator c1 = new SubstractionableCalculator(10, 20);
        c1.sum();
        c1.avg();
        c1.substract();
    }
}
```

- 하지만 위 코드는 오류 발생
  - 상위 클래스인 `Calculator`의 생성자가 존재하지 않는다는 오류
  - 하위 클래스 호출시 자동으로 상위 클래스의 기본 생성자를 호출. 만약 상위 클래스에 매개변수가 있는 생성자가 있으면 자바는 자동으로 기본 생성자를 만들어주지 않음. 존재하지 않는 생성자를 호출하려 하기 때문에 에러가 발생
  - 오류 해결을 위해 상위 클래스에 기본 생성자 추가

```java
class Calculator {
    int left, right;
     
    // 기본 생성자 추가
    public Calculator() {}
     
    public Calculator(int left, int right) {
        this.left = left;
        this.right = right;
    }
    
    ...
```

<br>

#### super

- 상위 클래스를 가리키는 키워드

- `super()` . 부모 클래스의 생성자를 의미. 부모 클래스의 기본 생성자가 없어져도 오류가 발생하지 않음

```java
class Calculator {
    int left, right;
    
    // 기본 생성자가 없어도 됨
    // public Calculator(){}
     
    public Calculator(int left, int right){
        this.left = left;
        this.right = right;
    }
     
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
class SubstractionableCalculator extends Calculator {
    public SubstractionableCalculator(int left, int right) {
        // super 키워드로 부모 클래스의 생성자를 가리킴
        super(left, right);
    }
 
    public void substract() {
        System.out.println(this.left - this.right);
    }
}
 
public class CalculatorConstructorDemo5 {
    public static void main(String[] args) {
        SubstractionableCalculator c1 = new SubstractionableCalculator(10, 20);
        c1.sum();
        c1.avg();
        c1.substract();
    }
}
```

<br>

***

### 3. overriding

- 상속할 때, 하위 클래스가 부모 클래스의 기본적인 동작방법을 변경할 수 있는 기능
- 메소드 오버라이딩

```java
// 계산기 예제
class Calculator {
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
 
class SubstractionableCalculator extends Calculator {
    // 부모 클래스의 sum() 메소드를 자식 클래스에서 변경하여 활용
    public void sum() {
        System.out.println("실행 결과는 " +(this.left + this.right)+"입니다.");
    }
     
    public void substract() {
        System.out.println(this.left - this.right);
    }
}
 
public class CalculatorDemo {
    public static void main(String[] args) {
        SubstractionableCalculator c1 = new SubstractionableCalculator();
        c1.setOprands(10, 20);
        c1.sum();
        c1.avg();
        c1.substract();
    }
}
```

<br>

#### 오버라이딩의 조건

1. 메소드의 이름
2. 메소드 매개변수의 숫자와 데이터 타입 그리고 순서
3. 메소드의 리턴 타입

```java
// avg() 메소드를 변경
class Calculator {
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
 
class SubstractionableCalculator extends Calculator {
     
    public void sum() {
        System.out.println("실행 결과는 " +(this.left + this.right)+"입니다.");
    }
     
    public int avg() {
        return (this.left + this.right)/2;
    }
     
    public void substract() {
        System.out.println(this.left - this.right);
    }
}
 
public class CalculatorDemo {
    public static void main(String[] args) {
        SubstractionableCalculator c1 = new SubstractionableCalculator();
        c1.setOprands(10, 20);
        c1.sum();
        c1.avg();
        c1.substract();
    }
}
```

- The **return** type is incompatible with Calculator.avg() 이라는 오류 발생
  - 부모 클래스의 avg() 메소드의 리턴 타입은 void
  - 자식 클래스의 avg() 메소드 리턴 타입이 int
  - 메소드 리턴 형식이 다르기 때문에 오류 발생

- 메소드의 서명(Signature)
  - 메소드의 형태를 정의하는 사항들

```java
// 메소드 서명을 같게 하여 오버라이딩하고, super 키워드를 활용하여 코드의 중복 제거
class Calculator {
    int left, right;
 
    public void setOprands(int left, int right) {
        this.left = left;
        this.right = right;
    }
 
    public void sum() {
        System.out.println(this.left + this.right);
    }
 	
    // return 타입을 int로 변경
    public int avg() {
        return ((this.left + this.right) / 2);
    }
}
 
class SubstractionableCalculator extends Calculator {
     
    public void sum() {
        System.out.println("실행 결과는 " +(this.left + this.right)+"입니다.");
    }
    
    // super 키워드로 코드 중복 제거
    public int avg() {
        return super.avg();
    }
     
    public void substract() {
        System.out.println(this.left - this.right);
    }
}
 
public class CalculatorDemo {
    public static void main(String[] args) {
        SubstractionableCalculator c1 = new SubstractionableCalculator();
        c1.setOprands(10, 20);
        c1.sum();
        System.out.println("실행 결과는" + c1.avg());
        c1.substract();
    }
}
```

<br>

***

### 4. overloading

- 이름이 같지만 시그니처가 다른 메소드를 중복으로 선언하는 방법을 메소드 오버로딩이라 함

```java
class Calculator{
    int left, right;
    int third = 0;
      
    public void setOprands(int left, int right){
        System.out.println("setOprands(int left, int right)");
        this.left = left;
        this.right = right;
    }
     
    public void setOprands(int left, int right, int third){
        System.out.println("setOprands(int left, int right, int third)");
        this.left = left;
        this.right = right;
        this.third = third;
    }
     
    public void sum(){
        System.out.println(this.left+this.right+this.third);
    }
      
    public void avg(){
        System.out.println((this.left+this.right+this.third)/3);
    }
}
  
public class CalculatorDemo {
      
    public static void main(String[] args) {
          
        Calculator c1 = new Calculator();
        
        // 매개변수 2개 설정
        c1.setOprands(10, 20);
        c1.sum();       
        c1.avg();
        
        // 매개변수 3개 설정
        c1.setOprands(10, 20, 30);
        c1.sum();       
        c1.avg();
         
    }
  
}
```

```java
// 결과
setOprands(int left, int right)
30
10
setOprands(int left, int right, int third)
60
20
```

<br>

#### 오버로딩의 규칙

- 매개변수가 다르면 이름이 같아도 서로 다른 메소드가 됨
- 매개변수가 같지만 리턴 타입이 다르다면 오류가 발생
- 메소드의 반환값은 메소드를 호출하는 시점에서 전달되지 않는 정보이기 때문에 오버로딩의 대상이 될 수 없음

<br>

#### overriding vs. overloading

- 오버라이딩 : 부모 클래스의 메소드 동작방법을 변경
- 오버로딩 : 다른 매개변수의 메소드를 여러개 만들 수 있는 것

<br>

***

### 참고 자료

[생활코딩 - JAVA](https://opentutorials.org/course/1223/)

