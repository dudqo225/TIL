# Java | Mockito 1

<br>

#### Mockito 란?

- Mock : 진짜 객체와 비슷하게 동작하지만, 프로그래머가 직접 그 객체의 행동을 관리하는 객체
- Mockito : Mock 객체를 쉽게 만들고 관리, 검증할 수 있는 방법을 제공함
  - 자바 개발자 50% 이상이 사용하는 Mock 프레임워크
  - 대체제
    - EasyMock
    - JMock
- 단위 테스트에 대한 고찰
  - https://martinfowler.com/bliki/UnitTest.html

<br>

#### Mockito 시작하기

- 스프링 부트 `2.2.x` 프로젝트 생성시 의존성 자동 추가됨

  - `spring-boot-starter-test`

- 없을 경우, 의존성 직접 추가

  - ```java
    // mockito core
    <dependency>
        <groupId>org.mockito</groupId>
        <artifactId>mockito-core</artifactId>
        <version>3.1.0</version>
        <scope>test</scope>
    </dependency>
    
    // mockito-junit-jupiter
    <dependency>
        <groupId>org.mockito</groupId>
        <artifactId>mockito-junit-jupiter</artifactId>
        <version>3.1.0</version>
        <scope>test</scope>
    </dependency>
    ```

- Mock 활용 테스트 작성 방법
  - Mock 만들기
  - Mock 동작 관리
  - Mock 행동 검증

- Reference
  - https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Mockito.html

<br>

#### Mock 객체 만들기

- `Mockito.mock()` 메서드로 만들기

  - ```java
    MemberService memberService = mock(MemberService.class);
    
    StudyRepository studyRepository = mock(StudyRepository.class);
    ```

- `@Mock` 애노테이션으로 만들기

  - JUnit 5 extension으로 `MockitoExtension` 사용해야 함

  - 필드 or 메소드 매개변수로 작성

  - ```java
    // 필드
    @ExtendWith(MockitoExtension.class)
    class StudyServiceTest {
    
        @Mock MemberService memberService;
    
        @Mock StudyRepository studyRepository;
    }
    
    // 메소드 매개변수
    @ExtendWith(MockitoExtension.class)
    class StudyServiceTest {
        
        @Test
        void createStudyService(@Mock MemberService memberService,
                                @Mock StudyRepository studyRepository) {
            StudyService studyService = new StudyService(memberService, studyRepository);
            assertNotNull(studyService);
        }
    
    }
    ```

<br>

#### Mock 객체 Stubbing

- Stubbing
  - 조작하는 것
- 모든 Mock 객체의 행동
  - Null을 리턴 (Optional 타입은 Optional.empty 리턴)
  - Primitive 타입은 기본 Primitive 값
  - Collection은 비어있는 Collection
  - void 메소드는 예외를 던지지 않고 아무런 일도 발생하지 X

- Mock 객체 조작
  - `when().thenReturn()`
  - 특정 매개변수를 받은 경우 특정 값을 리턴하거나 예외를 던지도록 할 수 있음
  - void 메소드의 특정 매개변수를 받거나 호출된 경우 예외를 발생시킬 수 있음
  - 동일한 매개변수로 메소드가 여러번 호출될 때 각각 다르게 행동하도록 조작할 수 있음

<br>

#### Mock 객체 Stubbing 연습

```java
Study study = new Study(10, "테스트");

// TODO memberService 객체에 findById 메소드를 1L 값으로 호출하면 Optional.of(member) 객체를 리턴하도록 Stubbing
when(memberService.findById(1L)).thenReturn(Optional.of(member));
// TODO studyRepository 객체에 save 메소드를 study 객체로 호출하면 study 객체 그대로 리턴하도록 Stubbing
when(studyRepository.save(study)).thenReturn(study);

studyService.createNewStudy(1L, study);

assertNotNull(study.getOwner());
assertEquals(member, study.getOwner());
```

<br>

#### Mock 객체 확인

- 특정 메소드가 특정 매개변수로 몇 번 호출되었는지 확인
  - `verify()`
- 어떤 순서대로 호출했는지
  - `inOrder()`
- 특정 시간 이내에 호출되었는지
- 특정 시점 후에 아무 일도 일어나지 않았는지

<br>

#### Mockito BDD 스타일 API

- BDD (Behavior Driven Development)

  - 애플리케이션이 **어떻게 행동해야 하는지**에 대한 공통된 이해를 구성하는 방법
  - TDD에서 착안

- 행동에 대한 스펙

  - Title
  - Narrative
    - As a / I wnat / so that
  - Acceptance Criteria
    - **Given / When / Then**

- **BddMockito** 클래스

  - when → given

    - ```java
      when(memberService.findById(1L)).thenReturn(Optional.of(member));
      when(studyRepository.save(study)).thenReturn(study);
      
      given(memberService.findById(1L)).willReturn(Optional.of(member));
      given(studyRepository.save(study)).willReturn(study);
      ```

  - verify → then

    - ```java
      verify(memberService, times(1)).notify(study);
      verifyNoMoreInterctions(memberService);
      
      then(memberService).should(times(1)).notify(study);
      then(memberService).shouldHaveNoMoreInteractions();
      ```

<br>

#### Mockito 연습문제

##### 다음 StudyService 코드에 대한 테스트를 Mockito를 사용해서 Mock 객체를 만들고 Stubbing과 Verifying을 사용해서 테스트를 작성하세요.

```java
// StudyService.java

public Study openStudy(Study study) {
  
    study.open();
    Study openedStudy = repository.save(study);
    memberService.notify(openedStudy);
    return openedStudy;
  
}
```

```java
//StudyServiceTest.java

@DisplayName("다른 사용자가 볼 수 있도록 스터디를 공개한다.")
@Test
void openStudy() {
  
    // Given
    StudyService studyService = new StudyService(memberService, studyRepository);
    Study study = new Study(10, "더 자바, 테스트");
  	
  	assertNull(study.getOpenedDateTime());
  
    // TODO studyRepository Mock 객체의 save 메소드를호출 시 study를 리턴하도록 만들기.
		given(studyRepository.save(study)).willReturn(study);
  
    // When
    studyService.openStudy(study);

    // Then
    // TODO study의 status가 OPENED로 변경됐는지 확인
    assertEquals(StudyStatus.OPENED, study.getStatus());
  
    // TODO study의 openedDataTime이 null이 아닌지 확인
  	assertNotNull(study.getOpenedDateTime());
  
    // TODO memberService의 notify(study)가 호출 됐는지 확인.
 		then(memberService).should().notify(study);
  
}
```