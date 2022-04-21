package me.junitstudy.junit;

import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assumptions.assumeTrue;

// 클래스의 모든 테스트 메소드에 적용됨
//@DisplayNameGeneration(DisplayNameGenerator.ReplaceUnderscores.class)
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
class StudyTest {

    // @Disabled // 실행하고싶지  않은 테스트에 작성
    @FastTest // @Tag("fast") 생략 가능
    @DisplayName("스터디 만들기") // 원하는 이름 작성 가능
    void create() {


//        assumeTrue("LOCAL".equalsIgnoreCase(System.getenv("TEST_ENV")));

//        assertTimeoutPreemptively(Duration.ofMillis(100), () -> {
//            new Study(10);
//            Thread.sleep(300);
//        });
//        assertTimeout(Duration.ofMillis(100), () -> {
//            new Study(10);
//            Thread.sleep(300);
//        });


//        IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> new Study(-10));
//        String message = exception.getMessage();
//        assertEquals("limit은 0보다 커야 한다.", exception.getMessage());


//        Study study = new Study(-10);
//        assertAll(
//                () -> assertNotNull(study),
//                () -> assertEquals(StudyStatus.DRAFT, study.getStatus(), () -> "스터디를 처음 만들면 DRAFT 상태다."), // 문자열 연산을 피하기 위해서(성능을 위함) 람다식으로 메시지 표현이 가능함
//                () -> assertTrue(study.getLimit() > 0, "스터디 최대 참석 가능 인원은 0보다 커야 한다.")
//        );
    }

    @SlowTest // @Tag("slow") 생략 가능
    @DisplayName("스터디 만들기222")
    void create1() {
        System.out.println("create1");
    }

    @DisplayName("스터디 만들기")
    @RepeatedTest(value = 10, name = "{displayName}, {currentRepetition}/{totalRepetition}")
    void repeatTest(RepetitionInfo repeatitionInfo) {
        System.out.println("test" + repeatitionInfo.getCurrentRepetition() + "/" +
                repeatitionInfo.getTotalRepetitions());
    }

    @DisplayName("스터디 만들기")
    @ParameterizedTest(name = "{index} {displayName} message={0}")
//    @ValueSource(strings = {"날씨가", "많이", "추워지고", "있네요"})
//    @CsvSource({"java, 10", })
    @ValueSource(ints = {10, 20, 40})
    void parameterizedTest(String message) {
        System.out.println(message);
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