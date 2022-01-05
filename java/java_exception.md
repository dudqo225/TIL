# JAVA | Exception

### 목차

> 1. 예외
> 2. 예외 던지기
> 3. 예외 만들기
> 4. 참고 자료

<br>

***

### 1. 예외

#### 예외란?

- Exception
- 프로그램을 만든 프로그래머가 상정한 정상적인 처리에서 벗어나는 경우에 이를 처리하기 위한 방법
- 오류 처리

<br>

#### try ~ catch

- try
  - 예외 상황이 발생할 것으로 예상되는 로직을 위치시킴
- catch
  - 예외가 발생했을 때 뒷수습을 위한 로직
- 즉, 오류가 발생하면 try 실행이 중단되고 catch 구문 안의 내용이 실행됨

<br>

#### 예외 클래스 & 인스턴스

```java
// 예제
public void divide(){
        try {
            System.out.print("계산결과는 ");
            System.out.print(this.left/this.right);
            System.out.print(" 입니다.");
        } catch(Exception e){
            System.out.println("오류가 발생했습니다 : "+e.getMessage());
        }
    }
```



- `Exception`
  - 자바 기본 클래스 - `java.lang` 에 소속되어 있음
  - 변수의 데이터 타입
  - Exception 클래스의 인스턴스를 전달
- `e`
  - 변수
  - `.getMessage()` - 오류의 원인을 사람이 이해하기 쉬운 형태로 리턴

<br>

#### 기본적인 catch 방법

##### .getMessage()

- 오류에 대한 기본적인 내용을 출력. 상세하지 않음

##### .toString()

- `.getMessage()` 보다 자세한 예외 정보를 제공

##### .printStackTrace()

- 리턴값이 없음
- 내부적으로 예외 결과를 화면에 출력
- 가장 자세한 예외 정보를 제공

<br>

#### finally

- 예외가 발생하는 것과 상관없이 언제나 실행되는 로직
- 작업의 뒷정리를 담당

<br>

### 2. 예외 던지기

- API를 사용할 때 설계자의 의도에 따라서 예외를 반드시 처리해야 하는 경우가 있음

- `Throw`
  - 문제 발생시 이에 대한 처리를 사용자에게 위임하겠다는 의미
  - 예외에 대한 처리를 반드시 해야 함
  - ex.
    - FileReader

<br>

#### throw와 throws

- `throw` 를 통해서 예외처리를 할 수 있음. 예외를 발생시키는 명령어

- `throws` 키워드를 통해서 다음 사용자에게 예외 처리를 넘김

<br>

### 3. 예외 만들기

#### 주요 Exception 리스트

| 예외                      | 상황                                        |
| ------------------------- | ------------------------------------------- |
| IllegalArgumentException  | 매개변수가 의도하지 않은 상황을 유발시킬 때 |
| IllegalStateException     | 메소드를 호출하기 위한 상태가 아닐 때       |
| NullPointerException      | 매개 변수 값이 null 일 때                   |
| IndexOutOfBoundsException | 인덱스 매개 변수 값이 범위를 벗어날 때      |
| ArithmeticException       | 산술적인 연산에 오류가 있을 때              |

<br>

#### 예외의 종류

- Throwable
  - 예외 클래스의 조상
  - 이 클래스를 직접 사용하지는 않음
- Error
  - 애플리케이션 혹은 애플리케이션이 동작하는 가상머신에 문제가 생겼을 때 발생하는 예외
  - 메모리가 부족한 경우..
    - 예외처리하지 말고 에러로 인해 애플리케이션이 중단되도록 내버려둬야함
- Exception
  - checked 예외
  - 반드시 예외처리 해야 함
- Runtime Exception
  - unchecked 예외
  - 해도되고 안해도 되는 예외

<br>

#### 나만의 예외 만들기

- 표준 예외 클래스외에 많은 예외 상황을 표현하려고 할 때
- 직접 예외를 만들 수 있음

<br>

***

### 4. 참고 자료

[생활코딩 - JAVA | 예외](https://opentutorials.org/course/1223/6228)