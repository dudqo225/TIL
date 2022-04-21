# Java | JUnit 3

<br>

### JUnit 5 확장 모델

- **Extension** 하나만 있음
  - JUnit 4는 @RunWith(Runner), TestRule, MethodRule 등이 있음
- 등록 방법
  - 선언적 등록 - `@ExtendWith`
  - 프로그래밍 등록 - `@RegisterExtension`
  - 자동 등록 - 자바 `ServiceLoader `

<br>

### JUnit 4 마이그레이션

- **junit-vintage-engine** 의존성을 추가하면 JUnit3, 4로 작성된 테스트를 실행할 수 있음
- JUnit 4의 `@Rule`은 기본적으로 지원하지 X
  - `junit-jupiter-migrationsupport` 모듈이 제공하는 **@EnableRuleMigrationSupport**를 사용하면 가능
    - ExternalResource
    - Verifier
    - ExpectedException

| JUnit 4                                    | JUnit 5                                        |
| ------------------------------------------ | ---------------------------------------------- |
| @Category(Class)                           | @Tag(String)                                   |
| @RunWith, @Rule, @ClassRule                | @ExtendWith, @RegisterExtension                |
| @Ignore                                    | @Disabled                                      |
| @Before, @After, @BeforeClass, @AfterClass | @BeforeEach, @AfterEach, @BeforeAll, @AfterAll |

<br>

### JUnit 5 연습문제

##### 1. 테스트 이름을 표기하는 방법으로 공백, 특수 문자 등을 자유롭게 쓸 수 있는 애노테이션은?

A. `@DisplayName`

<br>

##### 2.  JUnit 5, jupiter는 크게 세가지 모듈로 나눌 수 있습니다. 다음 중에서 테스트를 실행하는 런처와 테스트 엔진의 API를 제공하는 모듈은 무엇일까요?

보기. ① junit jupiter ② junit vintage **③ junit platform**

<br>

##### 3. JUnit 5에서 테스트 그룹을 만들고 필터링 하여 실행하는데 사용하는 애노테이션은?

A. `@Tag()`

<br>

##### 4. 다음 코드는 여러 Assertion을 모두 실행하려는 테스트 코드입니다. 빈칸에 적절한 코드는 무엇인가요?

```java
@Test
@DisplayName("스터디 만들기")
void create_new_study() {
    Study actual = new Study(1, "테스트 스터디");
    ________(
        () -> assertEquals(1, actual.getLimit()),
        () -> assertEquals("테스트 스터디", actual.getName()),
        () -> assertEquals(StudyStatus.DRAFT, actual.getStatus())
    );
}

```

A. **assertAll**

<br>

##### 5. 다음은 JUnit 5가 제공하는 애노테이션으로 컴포짓 애노테이션을 만드는 코드입니다. 이 애노테이션에 적절한 Rention 전략은 무엇인가요?

```java
@Target(ElementType.METHOD)
@Retention(______________)
@Test
@Tag("fast")
public @interface FastTest {
}
```

A. **RetentionPolicy.RUNTIME**

<br>

##### 6. 다음 중 JUnit 5가 제공하는 확장팩 등록 방법이 아닌것은?

보기. ① @ExtendWith **② @Rule** ③ @RegisterExtension ④ ServiceLoader

<br>

##### 7. 다음 코드는 유즈케이스 테스트를 작성한 것입니다. 다음 빈 칸에 적절한 코드는?

```java
@TestInstance(TestInstance.Lifecycle.________)
@TestMethodOrder(MethodOrderer.___________.class)
public class StudyCreateUsecaseTest {

    private Study study;

    @Order(1)
    @Test
    @DisplayName("스터디 만들기")
    public void create_study() {
        study = new Study(10, "자바");
        assertEquals(StudyStatus.DRAFT, study.getStatus());
    }

    @Order(2)
    @Test
    @DisplayName("스터디 공개")
    public void publish_study() {
        study.publish();
        assertEquals(StudyStatus.OPENED, study.getStatus());
        assertNotNull(study.getOpenedDateTime());
    }

}
```

A. **PER_CLASS** / **OrderAnnotation**

<br>

##### 8. 다음은 여러 매개변수를 바꿔가며 동일한 테스트를 실행하는 코드입니다. 빈칸에 적잘한 코드는?

```java
@Order(4)
@DisplayName("스터디 만들기")
@________________(name = "{index} {displayName} message={0}")
@CsvSource({"10, '자바 스터디'", "20, 스프링"})
void parameterizedTest(@___________(StudyAggregator.class) Study study) {
    System.out.println(study);
}

static class StudyAggregator implements ArgumentsAggregator {
    @Override
    public Object aggregateArguments(ArgumentsAccessor accessor, ParameterContext context) throws ArgumentsAggregationException {
        return new Study(accessor.getInteger(0), accessor.getString(1));
    }
}
```

A. **ParameterizedTest** / **AggregateWtih**