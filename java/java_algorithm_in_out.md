# JAVA | 알고리즘 입출력 방법 정리

### 목차

> 1. 입력
> 2. 출력
> 3. 참고 자료

<br>

***

알고리즘 문제를 풀 때 우리는 문제에 주어진 내용에 따라 입력값을 받아야 한다. 또한 알고리즘 로직을 짜고 이에 따른 출력값을 표시해야 한다.

파이썬에서는 간단하게 입력은 `input()` 으로, 출력은 `print()` 로 수행할 수 있지만 Java 언어에서는 입출력 방법이 다양하고 이에 따라서 불러와야 하는 클래스도 다양하다.

본 글에서는 자바를 활용한 알고리즘 문제 풀이 시, 사용할 수 있는 입출력 방법을 정리하고자 한다.

<br>

### 1. 입력

입력 방식으로는 대표적인 2가지가 있다.

1. `Scanner`

2. `BufferedReader`

<br>

#### Scanner

가장 기초적인 입력방법이다. 

Scanner에 대해서 알기 전에 InputStream과 System.in에 대해서 알아야 한다. 간단히 정리하자면,

**InputStream** - 바이트 단위로 데이터를 처리(가장 기본적인 입력 처리 스트림 - 반대로 출력 스트림은 OutputStream)

**System.in** - InputStream 타입의 정적 필드이다.

<br>

- 사용 방법
  1. `Scanner` 클래스 import
     - 이클립스 IDE를 사용할 때는 `Ctrl + Shift + O` 단축키로 클래스를 자동 import 할 수 있다.
  2. 객체 생성
     - `System.in` 은 입력 값을 Byte 단위로 읽는 것을 의미한다.
       - Java에서 가장 기본이 되는 입력 스트림을 활용하여 객체를 생성한다.
     - 객체명은 일반적으로 `in`, `scan`, `sc` 를 많이 쓴다.
  3. 입력 받기
     - 변수의 자료형에 맞는 메소드를 사용해야 한다.

```java
// Scanner 사용 예시

// 1. Scanner 클래스 import
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 2. 객체 생성
        Scanner sc = new Scanner(System.in);        

        int a, b;
        // 3. 입력 받기
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        System.out.println(a+b);
    }
}
```

<br>

- 변수 자료형에 따른 메소드

```java
// Reference Type
	// >> Class Type - String Class 
    
		String 문자열_space = sc.next();
		String 문자열_Enter = sc.nextLine();
		 
// Primitive Type
	// >> boolean Type
    
		boolean 부울 = sc.nextBoolean();
		
	// >> Numeric Type
		// >> >> Integer Type
        
		byte 바이트 = sc.nextByte();
		short 쇼트 = sc.nextShort();
		int 정수 = sc.nextInt();
		long 롱 = sc.nextLong();
		
		// >> >> Floating Point Type
        
		double 더블형 = sc.nextDouble();
		float 플롯 = sc.nextFloat();
```

<br>

- String 입력방법
  1. `sc.next()` - 문자열 입력시 공백 전까지만 받음
  2. `sc.nextLine()` - 문자열 입력시 Enter 입력 전까지만 받음
     - 대부분 문제에서 `nextLine()`을 사용함

<br>

#### BufferedReader

Scanner에 비해서 성능이 훨씬 우수한 입력 방법이다. 

Scanner는 입력값을 정규식 검사를 통해 Byte 단위 데이터→ 문자(character) 단위 데이터로 처리할 수 있도록 변환한다.

반면, BufferedReader는 정규식 검사 없이 Char Type의 데이터를 읽고, **버퍼**가 있는 스트림이기 때문에 버퍼에 많은 문자열을 저장했다가 한 번에 보낸다.

<br>

- 문자열 입력 받는 방법
  1. `readLine()` - 한 행을 읽음
     - 대부분 이 방법을 사용
  2. `read()` - 한 문자만 읽음

<br>

- 문자열을 분리하는 방법
  1. `StringTokenizer`
     - 성능 면에서 split()` 보다 우수함
     - 객체 생성시 `StringTokenizer("문자열", 구분자);` 로 생성
     - 구분된 변수는 `nextToken()` 으로 꺼내면 문자열을 반환함
     - 반환한 문자열을 `Integer.parseInt()`로 int 형 변환해준다.
  2. `split()`

```java
// BufferedReader 사용 예시 - StringTokenizer로 문자열 분리
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
 
public class Main {
 
	public static void main(String[] args) throws IOException {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
 		String str = br.readLine();
		StringTokenizer st = new StringTokenizer(str," ");
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		
		System.out.println(a+b);
    }
}
```

```java
// BufferedReader 사용 예시 - split()으로 문자열 분리
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main {
 
	public static void main(String[] args) throws IOException {
		     
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] str = br.readLine().split(" ");
		int a = Integer.parseInt(str[0]);
		int b = Integer.parseInt(str[1]);
		
		System.out.println(a+b);
	}
}
```

<br>

***

### 2. 출력

출력 방법도 다양하게 존재한다.

그 중에서 우리는 대표적으로 `print()` 와 `println()` 을 볼 수 있는데, 이 중에서 `println()` 을 가장 많이 사용한다.

**print()** - 개행 없이 출력

**println()** - 출력시 줄 바꿈(`\n`)이 포함되어 있음

따라서, 알고리즘 문제를 풀 때는 가장 기본적이면서 가장 많이 사용되는 `println()` 을 사용하면 된다.

<br>

그런데, String 객체를 출력할 때 굳이 반복적으로 println() 을 사용해야 할까? 메모리, 시간적인 부분에서 성능 저하가 발생할 것이다. 이때, 사용할 수 있는 것이 바로 `StringBuilder` 이다.

<br>

#### StringBuilder

String과 문자열을 더할 때 새로운 객체를 생성하는 것이 아닌 기존 데이터에 계속 더해주는 방식을 사용하기 때문에 속도가 빠르고 메모리적으로 부하가 적다. 긴 문자열을 더해야 하거나, 여러 줄을 출력하고자 할 때 사용하면 된다.

<br>

- 사용 방법
  1. `StringBuilder` 타입으로 새로운 객체 생성
  2. `.append()` 메소드로 원하는 데이터를 더해준다.
  3. 출력시 `toString()` 을 사용한다.
     - 사용하지 않아도 출력 결과가 나온다.
     - 이유는, `StringBuilder` 자체에 `toString()`이 오버라이딩 되어 있기 때문

```java
// StringBuilder 사용 예시 - 1 ~ N까지 정수 출력하기
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		
		for (int i = 1; i <= N; i++) {
			sb.append(i + "\n");
		}
        
		System.out.println(sb);
	}
}
```

<br>

***

### 3. 참고 자료

https://onlyfor-me-blog.tistory.com/317

https://hardlearner.tistory.com/288

https://commin.tistory.com/21

https://st-lab.tistory.com/12