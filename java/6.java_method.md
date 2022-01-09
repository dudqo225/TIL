# JAVA | Method

### 목차

>1. 메소드
>2. 메소드의 입력과 출력
>3. 참고자료



### 1. 메소드

- 메소드(method)는 코드를 재사용할 수 있게 해줌



#### 정의와 호출

- 정의 : 직접 메소드를 만드는 것
- 호출 : 만들어진 메소드를 실행하는 것



#### main 메소드

- `public static void main(String[] args)`
- 이것은 하나의 **약속**



```java
// 메소드 예시
public class MethodDemo3 {
    public static void numbering() {
        int i = 0;
        while (i < 10) {
            System.out.println(i);
            i++;
        }
    }
 
    public static void main(String[] args) {
        numbering();
        numbering();
        numbering();
        numbering();
        numbering();
    }
}
```

- `numbering()` 이라는 하나의 메소드를 작성하고, 이 메소드를 `main()` 메소드에서 재사용한다.



### 2. 메소드의 입력과 출력

#### 매개변수(parameter)

- 메소드의 입력 값.
- 입력값에 따라서 다른 출력 값을 갖도록 하는 메소드를 정의할 수 있음

```java
// 매개변수 활용 예시
public static void numbering(int limit) {
    int i = 0;
    while (i < limit) {
        system.out.printIn(i);
        i++;
    }
}

public static void main(String[] args) {
    numbring(5);
}
```

- `numbering(5)` 의 숫자 5는 numbering 메소드가 호출될 때 `int limit` 변수의 값이 된다.
- `int limit` 와 같이, 입력한 값을 로직으로 매개하는 변수를 **매개변수(Parameter)** 라고 함
- 메소드를 호출할 때 전달된 값 `5` 를 **인자(Argument)** 라고 함



#### 복수의 인자

- 메소드로 여러개의 입력값을 전달하고자 할 때 인자를 여러개 활용할 수 있다.

```java
// 복수 인자 활용 예시
public static void numbering(int init, int limit) {
    int i = init;
    while (i < limit) {
        System.out.printIn(i);
        i++;
    }
}

publi static void main(String[] args) {
    numbering(1, 5);
}
```

- 숫자 `1`과 매개변수 `int init` 이 연결되고, 숫자 `5`와 매개변수 `int limit`이 연결됨



#### return

- 메소드 내의 `return`을 사용하면 그 뒤에 따라오는 값을 메소드의 결과로 반환함
- **✨ return을 통해서 반환할 값의 데이터 형식을 메소드 이름 옆에 명시해 주어야 함!!!**

```java
// return 예시

public static String numbering(int init, int limit) {
    int i = init;
    String output = "";
    while (i < limit) {
        output += i;
        i++;
    }
    return output;
}

public static void main(String[] args) {
    String result = numbering(1, 5);
    System.out.printIn(result);
}
```

- 메소드가 리턴할 값의 데이터 타입을 정확히 명시함으로써 `numbering()` 메소드가 반드시 String(문자열) 값을 리턴한다는 것을 보장할 수 있다.
- 하지만 python, javascript 처럼 타입을 명시하지 않아도 되는 것에 익숙한 사람에게는 불편할 수 있다. 모든 것에 장.단점이 있기 마련!!!
- 반환 값이 없다면 `void` 를 적어준다.



##### 메소드를 중단시키는 return

- `return` 은 값을 반환하는 동작을 한다.
- 또한, 메소드를 중단시키는 역할도 수행한다.



##### 복수의 return

- 배열을 리턴하면 여러 개의 데이터를 처리할 수 있음

```java
// 예시
public static String[] getMembers() {
    String[] members = { "손흥민", "황의조", "박지성"};
    return members;
}

public static void main(String[] args) {
    String[] members = getMembers();
}
```



### 참고자료

[생활코딩 - JAVA | 메소드](https://opentutorials.org/course/1223/5369)

