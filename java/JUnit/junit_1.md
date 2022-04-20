# Java | JUnit 1

<br>

### JUnit5

- 단위 테스트를 작성하는 자바 개발자의 93%가 사용하는 테스트 프레임워크
  - 대체제 : `TestNG`, `Spock`...
- Spring Boot 버전이 `2.2.X` 로 올라가면서 JUnit의 버전도 `5` 로 의존성 자동 추가됨
- JUnit4 와의 차이점
  - 모듈화되어 있음
    - **JUnit Platform**
      - 테스트를 실행해주는 런처 제공
      - TestEngine API 제공
    - **Jupiter**
      - **TestEngine APi 구현체 - JUnit5**
    - Vintage
      - TestEngine APi 구현체 - JUnit4, JUnit3
- 메소드 생성시 `public` 붙일 필요 없음

<br>

#### 기본 Annotation

```java
class StudyTest {

    @Test
    @Disabled // 실행하고 싶지 않은 테스트에 작성
    void create() {
        Study study = new Study();
        assertNotNull(study);
        System.out.println("create");
    }

    @Test
    void create1() {
        System.out.println("create1");
    }

    @BeforeAll
    // 모든 테스트 실행전 딱 1번만 호출되는 함수. static void로 작성. return값 없음
    static void beforeAll() {
        System.out.println("before all");
    }

    @AfterAll
    // 모든 테스트 실행후 딱 1번만 호출됨. static void로 작성. return값 없음
    static void afterAll() {
        System.out.println("after all");
    }
    
    @BeforeEach
    // 각 테스트 실행 전에 한번씩 호출됨
    void beforeEach() {
        System.out.println("Before each");
    }
    
    @AfterEach
    // 각 테스트 실행 후에 한번씩 호출됨
    void afterEacth() {
        System.out.println("After each");
    }
}
```

<br>

#### 테스트 이름 표기하기

- **@DisplayNameGeneration**
  - Method, Class 레퍼런스를 사용하여 테스트의 이름을 표기하는 방법
  - 기본 구현체로 `ReplaceUnderscores` 제공
    - `_` 언더스코어를 띄어쓰기로 변환하여 출력
- **DisplayName**
  - 테스트 이름을 보다 쉽게 표현할 수 있는 방법을 제공
  - `@DisplayNameGeneration` 보다 우선순위가 높음

<br>

#### Assertion

- **org.junit.jupiter.api.Assertion.***
  - `assertEquals(expected, actual)` - 실제값이 기대값과 같은지 확인
  - `assertNotNull(actual)` - 값이 `null`이 아닌지 확인
  - `assertTrue(boolean)` - 다음 조건이 참(true)인지 확인
  - `assertAll(executables...)` - 모든 구문 확인
  - `assertThrows(expectedType, executable)` - 예외 발생 확인
  - `assertTimeout(duration, executable)` - 특정시간 안에 실행 완료되는지 확인
- 마지막 매개변수로 `Supplier<String>` 타입의 인스턴스를 람다 형태로 작성할 수 있음
  - 복잡한 메시지를 생성해야 할 때, 테스트가 실패한 경우에만 해당 메시지를 만들게 할 수 있음
    - **성능 개선**

- 이외에 `AssertJ`, `Hemcrest`, `Truth` 등의 라이브러리 사용 가능