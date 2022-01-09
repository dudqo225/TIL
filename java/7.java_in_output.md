# JAVA | 입력과 출력 In & Output

### 목차

>1. String[] args
>2. 앱 실행 중 입력 받기
>3. 참고 자료



### 1. String[] args

- 자바에서는 에플리케이션을 실행할 때 `main` 메소드가 호출되면서 프로그램이 구동하게 됨
- 이 때, `String[] args` 는 입력 값의 파라미터로 동작함
- 메소드가 호출될 때 전달된 입력값을 메소드 내부로 전달하는 역할을 수행
- `String[]` 은 문자열을 담고 있는 배열. `args.length`는 배열의 길이를 의미함

```java
// 예시
package org.opentutorials.javatutorials.io;

class InputDemo {
    public static void main(String[] args) {
        System.out.printIn(args.length);
    }
}
```

```java
// 위 코드를 컴파일
javac InputDemo.java

    
// InputDemo 프로그램 실행
java InputDemo 1 2 3 4 5 6;

// 실행 결과
6
```



### 2. 앱 실행 중 입력 받기

- 자바앱이 실행되고 있는 동안 사용자 입력을 받는 방법
- 자바 기본 라이브러리 중 `scanner` 활용

```java
// Scanner 활용 예시
package org.opentutorials.javatutorials.io;

import java.util.scanner;

public class ScannerDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = sc.nextInt();
        System.out.printIn(i*1000);
        sc.close();
    }
}
```

- `sc.nextInt()` : 사용자의 입력이 있을 때까지 변수 i에 값을 할당하지 않고 대기상태에 머무름
- 키보드에 데이터를 입력하고 엔터를 누르면 i에 값이 담기고 `i*1000`이 실행되면서 입력값 i에 1000 곱한 값이  화면에 출력됨



```java
// Scanner 활용 예시2
package org.opentutorials.javatutorials.io;

import java.util.scanner;

public class ScannerDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()) {
            System.out.printIn(sc.nextInt()*1000);
        }
        sc.close();
    }
}
```

- `sc.hasNextInt()` : 입력값이 생기기 전까지 실행을 유보시키는 역할
  - 입력값이 int 형이 아닐 경우 false 리턴, int 로 표현할 수 있는 숫자형인 경우 true 리턴



### 참고 자료

[생활코딩 - JAVA | 입력과 출력](https://opentutorials.org/course/1223/5575)