# Spring | 스프링 입문

### 목차

> 1. Spring 프로젝트 생성
> 2. 스프링 웹 개발 기초
> 3. 회원 관리 예제 - 백엔드 개발하기
> 4. 스프링 빈과 의존관계
> 5. 웹 MVC 개발
> 6. 스프링 DB 접근 기술
> 7. AOP
> 8. 참고 자료

<br>

***

### 1. Spring 프로젝트 생성

- 프로젝트 환경
  - Project : Gradle
  - Spring Boot: 2.6.2
  - Language: Java
  - Packaging : Jar
  - Java : 11
- Dependencies : Spring Web, Thymeleaf

- https://start.spring.io/ 
  - 위 페이지에서 쉽고 빠르게 Spring 프로젝트를 생성할 수 있음

<br>

```java
// build.gradle

plugins {
	id 'org.springframework.boot' version '2.6.2'
	id 'io.spring.dependency-management' version '1.0.11.RELEASE'
	id 'java'
}

group = 'hello'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '11'

repositories {
	mavenCentral()
}

dependencies {
	implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
	implementation 'org.springframework.boot:spring-boot-starter-web'
	implementation 'org.springframework.boot:spring-boot-devtools'
	testImplementation 'org.springframework.boot:spring-boot-starter-test'
}

test {
	useJUnitPlatform()
}

```

<br>

#### 라이브러리 살펴보기

- ##### 스프링 부트 라이브러리

  - spring-boot-starter-web
    - spring-boot-starter-tomcat :  톰캣(웹서버)
    - spring-webmvc : 스프링 웹 MVC
  - spring-boot-starter-thymeleaf : 타임리프 템플릿 엔진 (View)
  - spring-boot-starter(공통) : 스프링 부트 + 스프링 코어 + 로깅
    - spring-boot
      - spring-core
    - spring-boot-starter-logging
      - logback, slf4j

- ##### 테스트 라이브러리

  - spring-boot-starter-test
    - junit : 테스트 프레임워크
    - mockito : 목 라이브러리
    - asssertj : 테스트 코드 작성을 편하게 도와주는 라이브러리
    - spring-test : 스프링 통합 테스트 지원

<br>

#### 빌드하고 실행하기

1. 콘솔로 이동
2. `./gradlew build`
3. `cd build/libs`
4. `java -jar hello-sprig-0.0.1-SNAPSHOT.jar`
5. 실행 확인

<br>

***

### 2. 스프링 웹 개발 기초

- 정적 컨텐츠
- MVC와 템플릿 엔진
- API

<br>

#### 정적 컨텐츠

- 웹 브라우저에서 서버에 요청을 보내면 `static/` 폴더 하위에 있는 html 페이지를 응답한다. 

![image-20220109140655184](spring_스프링입문.assets/image-20220109140655184.png)

<br>

<br>

#### MVC와 템플릿 엔진

- MVC 란?
  - Model
  - View
  - Controller

<br>

##### Controller

```java
@Controller
public class HelloController {
    
    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model) {
       model.addAttribute("name", name);
       return "hello-template";
    }
}
```

##### View

- `resources/template/hello-template.html`

```html
<html xmlns:th="http://www.thymeleaf.org">
<body>
	<p th:text="'hello ' + ${name}">hello! empty</p>
</body>
</html>
```

![image-20220109140934530](spring_스프링입문.assets/image-20220109140934530.png)

- 웹 브라우저에서 `hello-mvc` 경로에 `name` 파라미터를 같이 전달하면 helloController라는 **Controller** 에서 `@GetMapping` 어노테이션으로 해당하는 요청과 일치하는 코드를 찾아 실행한다. 위 예시에서 `"hello-template"` 를 리턴하는데, 이는 **viewResolver**가  `resources/template/` 경로의 동일한 이름을 가진 html 파일을 찾아서 클라이언트에게 응답하는 구조를 보인다.

<br>

<br>

#### API

- 가장 많이 사용하는 개발 방식 (RESTful API, etc)
- `@ResponseBody` 문자 or 객체 반환
  - 문자 내용을 직접 반환
  - **Json 형태의 객체를 반환**

<br>

##### @ResponseBody 문자 반환

- viewResolver를 사용하지 않는다.
- HTTP Body에 문자 내용을 직접 반환함

```java
// 문자 반환
@Controller
public class HelloController {
    
    @GetMapping("hello-string")
    @ResponseBody
    public String helloString(@RequestParam("name") String name) {
        return "hello " + name;
    }
}
```

<br>

##### @ResponseBody 객체 반환

- 객체를 반환하면 Json으로 변환됨

```java
@Controller
public class HelloController {
    
    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello;
    }
    
    static class Hello {
        private String name;
        
        public String getName() {
            return name;
        }
        
        public void setName(String name) {
            this.name = name;
        }
    }
}
```

<br>

##### @ResponseBody 사용 원리

![image-20220109141832390](spring_스프링입문.assets/image-20220109141832390.png)

- @ResponseBody를 사용
  - HTTP Body에 문자 내용을 반환
  - `viewResolver` 대신 `HttpMessageConverter`가 동작함
  - 문자 처리 : `StringHttpMessageConverter`
  - 객체 처리 : `MappingJackson2HttpMessageConverter`
  - byte 처리 등 기타 여러가지 HttpMessageConverter가 등록되어 있다.
  - 클라이언트의 HTTP Accept 헤더와 서버의 컨트롤러 반환 타입 정보, 2가지를 조합해서 `HttpMessageConverter`가 선택된다.

<br>

***

### 3. 회원 관리 예제 - 백엔드 개발하기

- 3-1. 비즈니스 요구사항 정리
- 3-2. 회원 도메인과 리포지토리 만들기
- 3-3. 회원 리포지토리 테스트 케이스 작성
- 3-4. 회원 서비스 개발
- 3-5. 회원 서비스 테스트

<br>

#### 3-1. 비즈니스 요구사항 정리

- 데이터
  - 회원 ID
  - 이름
- 기능
  - 회원 등록
  - 회원 조회
- 아직 데이터 저장소(DB)가 선정되지 않음

<br>

##### 일반적인 웹 애플리케이션 계층 구조

![image-20220109143350838](spring_스프링입문.assets/image-20220109143350838.png)

- 컨트롤러 : 웹 MVC의 C. Controller 역할
- 서비스 : 핵심 비즈니스 로직 구현
- 리포지토리 : DB에 접근, 도메일 객체를 DB에 저장하고 관리
- 도메인 : 비즈니스 도메인 객체
  - 예) 회원, 주문, 쿠폰 등 DB에 저장되고 관리됨

![image-20220109164935623](spring_스프링입문.assets/image-20220109164935623.png)

<br>

##### 회원 관리 예제 클래스 의존관계

![image-20220109143510851](spring_스프링입문.assets/image-20220109143510851.png)

- 아직 데이터 저장소가 선정되지 않았기 때문에, 인터페이스로 구현하고 구현 클래스를 변경할 수 있도록 설계
- 데이터 저장소(DB)는 RDB, NoSQL 등 다양한 저장소를 고려중인 상황으로 가정함
- 개발 진행을 위하여 초기 개발 단계에서는 **구현체로 가벼운 메모리 기반의 데이터 저장소** 사용

<br>

<br>

#### 3-2. 회원 도메인과 리포지토리 만들기

##### 회원 객체

```java
package hello.hellospring.domain;

public class Member {
    
    priavte Long id;
    private String name;
    
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
}
```

##### <br>

##### 회원 리포지토리 인터페이스

```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberRepository {
    
    Member save(Member member);
    Optional<Member> findById(Long id);
    Optional<Member> findByName(String name);
    List<Member> findAll();
}
```

<br>

##### 회원 리포지토리 메모리 구현체

```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.util.*;

public class MemoryMemberRepository implements MemberRepository{

    private static Map<Long, Member> store = new HashMap<>();
    private static long sequence = 0L;

    @Override
    public Member save(Member member) {
        member.setId(++sequence);
        store.put(member.getId(), member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
        return store.values().stream()
                .filter(member -> member.getName().equals(name))
                .findAny();
    }

    @Override
    public List<Member> findAll() {
        return new ArrayList<>(store.values());
    }
    
    public void clearStore() {
        store.clear();
    }
}
```

<br>

<br>

#### 3-3. 회원 리포지토리 테스트 케이스 작성

- 일반적으로 자바 main 메서드나 웹 애플리케이션 컨트롤러를 통해서 개발한 기능을 테스트하기도 한다.
- 하지만 이러한 방법은 준비 및 실행 시간이 오래 걸리고, 반복 실행이 어려우며 여러 테스트를 한번에 실행하기 어렵다는 단점이 있다.
- **JUnit** 프레임워크를 사용하면 테스트를 한번에 실행할 수 있다.

<br>

##### 회원 리포지토리 메모리 구현체 테스트

- `src/test/java` 하위 폴더에 생성한다.

```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

class MemoryMemberRepositoryTest {

    MemoryMemberRepository repository = new MemoryMemberRepository();

    @AfterEach
    public void afterEach() {
        repository.clearStore();
    }

    @Test
    public void save() {
        Member member = new Member();
        member.setName("spring");

        repository.save(member);

        Member result = repository.findById(member.getId()).get();
        assertThat(member).isEqualTo(result);

    }

    @Test
    public void findByName() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        Member result = repository.findByName("spring1").get();

        assertThat(result).isEqualTo(member1);
    }

    @Test
    public void findAll() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        List<Member> result = repository.findAll();

        assertThat(result.size()).isEqualTo(2);
    }
}
```

- `@AfterEach`
  - 한 번에 여러개의 테스트를 진행하면 메모리 DB에 직전 테스트 결과가 남을 수 있다.
  - 이전 테스트 결과 때문에 다음 테스트가 실패할 가능성이 있다.
  - @AfterEach 어노테이션을 사용하여 각 테스트가 종료될 때마다 이 기능을 실행한다. 위 코드에서는 메모리 DB에 저장된 데이터를 삭제한다.
    - `MemoryMemberRepository` 클래스에 `clearStore()` 메소드를 만들어야 한다.
- 각 테스트는 독립적으로 실행되어야 한다. 테스트 순서에 의존관계가 있는 테스트는 좋은 테스트가 아니다.

<br>

#### 3-4. 회원 서비스 개발

```java
package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;

import java.util.List;
import java.util.Optional;

public class MemberService {

    private final MemberRepository memberRepository = new
MemoryMemberRepository();

    // 회원 가입
    public Long join(Member member) {

        // 중복 회원 x
        validateDuplicateMember(member);

        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicateMember(Member member) {
        memberRepository.findByName(member.getName())
                .ifPresent(m -> {
                    throw new IllegalStateException("이미 존재하는 회원입니다.");
                });
    }

    // 전체 회원 조회
    public List<Member> findMembers() {
         return memberRepository.findAll();
    }
    
    // 특정 회원 조회
    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }
}
```

<br>

#### 3-5. 회원 서비스 테스트

- **DI (Dependency Injection)**

  - 기존에는 회원 서비스(`MemberService`)가 메모리 회원 리포지토리(`MemoryMemberRepository`) 를 직접 생성하게 했다.
  - 회원 리포지토리 코드가 회원 서비스 코드를 DI 가능하게 변경한다.

  ```java
  // 기존
  public class MemberService {
  
      private final MemberRepository memberRepository = new
  MemoryMemberRepository();
  }
  ```

  ```java
  // 변경 - DI
  public class MemberService {
  
      private final MemberRepository memberRepository;
  
      public MemberService(MemberRepository memberRepository) {
          this.memberRepository = memberRepository;
      }
  }
  ```

<br>

##### 회원 서비스 테스트

```java
package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemoryMemberRepository;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertThrows;

class MemberServiceTest {

    MemberService memberService;
    MemoryMemberRepository memberRepository;

    @BeforeEach
    public void beforeEach() {
        memberRepository = new MemoryMemberRepository();
        memberService = new MemberService(memberRepository);
    }

    @AfterEach
    public void afterEach() {
        memberRepository.clearStore();
    }

    @Test
    void 회원가입() {
        // Given
        Member member = new Member();
        member.setName("spring");

        // When
        Long saveId = memberService.join(member);


        // Then
        Member findMember = memberService.findOne(saveId).get();
        assertThat(member.getName()).isEqualTo(findMember.getName());
    }

    @Test
    public void 중복_회원_예외() {
        // Given
        Member member1 = new Member();
        member1.setName("spring");

        Member member2 = new Member();
        member2.setName("spring");

        // When
        memberService.join(member1);
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2));
        assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");

    @Test
    void findMembers() {
    }

    @Test
    void findOne() {
    }
}
```

- `@BeforeEach`
  - 각 테스트 실행 전 호출 됨
  - 테스트가 서로 영향이 없도록 새로운 객체를 매번 새롭게 생성하고, 의존관계도 새롭게 맺어줌

<br>

***

### 4. 스프링 빈과 의존관계

- 4-1. 컴포넌트 스캔과 자동 의존관계 설정
- 4-2. 자바 코드로 직접 스프링 빈 등록하기

<br>

#### 4-1. 컴포넌트 스캔과 자동 의존관계 설정

회원 컨트롤러가 회원 서비스와 회원 리포지토리를 사용할 수 있도록 **의존관계**를 준비한다.

##### 컴포넌트 스캔 원리

- `@Component` : 어노테이션이 있으면 스프링 빈으로 자동 등록됨
  - `@Controller` : 컴포넌트 스캔을 통해 컨트롤러를 스프링 빈으로 자동 등록함
  - `@Service` : 서비스 등록
  - `@Repository` : 리포지토리 등록

<br>

##### 회원 컨트롤러에 의존관계 추가

```java
package hello.hellospring.controller;

import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

@Controller
public class MemberController {

    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }
}
```

- `@Autowired`
  - 생성자에 어노테이션이 있으면 스프링이 연관된 객체를 스프링 컨테이너에서 찾아서 넣어준다.
  - 이렇듯 객체 의존관계를 외부에서 넣어주는 것을 **DI (Dependency Injection)** 의존성 주입이라고 한다.

<br>

##### 회원 서비스 스프링 빈 등록

```java
@Service
public class MemberService {

    private final MemberRepository memberRepository;

    @Autowired
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }
    
    ...
}
```

- 생성자에 `@Autowired` 를 사영하면 객체 생성 시점에 스프링 컨테이너에서 해당 스프링 빈을 찾아서 주입한다.
- 생성자가 한 개만 있으면 `@Autowired` 어노테이션을 생략할 수 있다

<br>

##### 회원 리포지토리 스프링 빈 등록

```java
@Repository
public class MemoryMemberRepository implements MemberRepository {}
```

<br>

🎈 스프링은 컨테이너에 빈을 등록할 때, 기본적으로 **싱글턴**으로 등록한다. 

싱글턴 패턴(Singleton Pattern) 이란 생성자가 여러 차례 호출되더라도 **실제 생성되는 객체는 단 하나**이고, 최초 생성 이후에 호출된 생성자는 최초의 생성자가 생성한 객체를 리턴하는 것이다.

요청이 매우 많은 트래픽 사이트에서 객체를 매번 새롭게 생성하면 메모리 낭비가 심하기 때문에 일반적으로 싱글턴 패턴을 따른다.

<br>

#### 4-2. 자바 코드로 직접 스프링 빈 등록하기

회원 서비스와 회원 리포지토리의 `@Service` `@Repository` `@Autowired` 등의 어노테이션을 제거하고 직접 설정하는 방법

```java
// hello.hellospring 패키지 내에 SpringConfig 클래스 파일 생성
package hello.hellospring;

import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import hello.hellospring.service.MemberService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SpringConfig {

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }
}

```

- XML 로 설정하는 방식도 있지만 잘 사용하지 않음
- DI 방식은 필드 주입, setter 주입, 생성자 주입 3가지가 있다.
  - 의존관계가 실행 중에 동적으로 변하는 경우는 거의 없으므로 **생성자 주입** 방법을 사용한다.
- 정형화된 컨트롤러, 서비스, 리포지토리의 경우 **컴포넌트 스캔 방식**을 사용. 정형화되지 않거나 상황에 따라 구현 클래스를 변경해야 하는 경우 **스프링 빈으로 등록**

<br>

***

### 5. 웹 MVC 개발

- 5-1. 홈 화면 추가
- 5-2. 등록
- 5-3. 조회

<br>

#### 5-1. 홈 화면 추가

##### 홈 컨트롤러 추가

- `HomeController` 클래스 파일 생성

```java
package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home() {
        return "home";
    }
}
```

- `resources/template/` 하위 경로에 home.html 파일 생성

```java
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<body>
<div class="container">
    <div>
        <h1>Hello Spring</h1>
        <p>회원 기능</p>
        <p>
            <a href="/members/new">회원 가입</a>
            <a href="/members">회원 목록</a>
        </p>
    </div>
</div>
</body>
</html>
```

- 컨트롤러가 정적 파일보다 우선순위가 높기 때문에 기존 `static/index.html` 파일이 아닌 `resources/template/home.html` 파일을 응답한다.

<br>

#### 5-2. 등록

##### 회원 등록 폼 개발

- 회원 등록 폼 컨트롤러 

```java
@Controller
public class MemberController {

    ...

    @GetMapping("/members/new")
    public String createForm() {
        return "members/createMemberForm";
    }

}
```

- 회원 등록 폼 HTML
  - `resources/templates/members/createMemberForm.html`

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<body>
<div class="container">
    <form action="/members/new" method="post">
        <div class="form-group">
            <label for="name">이름</label>
            <input type="text" id="name" name="name" placeholder="이름을입력하세요">
        </div>
        <button type="submit">등록</button>
    </form>
</div> <!-- /container -->
</body>
</html>
```

<br>

##### 회원 등록 컨트롤러

- 웹 등록 화면에서 POST 방식으로 데이터를 전달 받을 폼 객체

```java
// MemberForm 클래스 파일 생성
package hello.hellospring.controller;

public class MemberForm {
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

- 회원 컨트롤러에서 회원을 실제 등록하는 기능 추가

```java
@PostMapping("/members/new")
public String create(MemberForm form) {

    Member member = new Member();
    member.setName(form.getName());

    memberService.join(member);

    return "redirect:/";
}
```

<br>

#### 5-3. 조회

##### 회원 컨트롤러에서 조회 기능

```java
@GetMapping("/members")
public String list(Model model) {
    List<Member> members = memberService.findMembers();
    model.addAttribute("members", members);
    return "members/memberList";
}
```

##### 회원 리스트 HTML (View)

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<body>
<div class="container">
    <div>
        <table>
            <thead>
            <tr>
                <th>#</th>
                <th>이름</th>
            </tr>
            </thead>
            <tbody>
            <tr th:each="member : ${members}">
                <td th:text="${member.id}"></td>
                <td th:text="${member.name}"></td>
            </tr>
            </tbody>
        </table>
    </div>
</div> <!-- /container -->
</body>
</html>
```

<br>

***

### 6. 스프링 DB 접근 기술

- 6-1. H2 데이터베이스 설치
- 6-2. 순수 Jdbc
- 6-3. 스프링 통합 테스트
- 6-4. 스프링 JdbcTemplate
- 6-5. JPA
- 6-6. 스프링 데이터 JPA

<br>

#### 6-1. H2 데이터베이스 설치

개발 or 테스트 용도로 가볍고 편리한 DB, 웹 화면 제공

<img src="spring_스프링입문.assets/image-20220110202546311.png" alt="image-20220110202546311" style="zoom: 50%;" />

- 사용방법
  - https://www.h2database.com 페이지에서 다운로드 및 설치
  - 실행 : `./h2.bat`
  - DB 파일 생성
    - `jdbc:h2:~/test`
    - 폴더 내에 `~/test.mv.db` 파일 생성 확인
    - `jdbc:h2:tcp://localhost/~/test` 경로로 접속

<br>

##### 테이블 생성하기

- H2 DB에 member 테이블 생성
- 추후 테이블 관리를 위해 스프링 프로젝트 루트에 `sql/ddl.sql` 파일을 작성

```sql
drop table if exists member CASCADE;
create table member
(
 id bigint generated by default as identity,
 name varchar(255),
 primary key (id)
);
```

<br>

#### 6-2. 순수 Jdbc

##### 환경설정

- build.gradle 파일에 jdbc, h2 db 관련 라이브러리 추가

```java
implementation 'org.springframework.boot:spring-boot-starter-jdbc'
runtimeOnly 'com.h2database:h2'
```

<br>

- 스프링 부트 데이터베이스 연결 설정 추가
  - `resource/application.properties

```java
spring.datasource.url=jdbc:h2:tcp://localhost/~/test
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.username=sa
```

<br>

##### Jdbc 리포지토리 구현

- Jdbc API로 직접 코딩하는 방식은 오래된 방식이다. 코드의 직접 구현보다는 이러한 방식이 있었다는 점만 기억하고 넘어가자.

Jdbc 회원 리포지토리

코드는 hello-spring 프로젝트 폴더 내의 `src/main/java/hello.hellospring/repository/JdbcMemberRepository` 클래스 파일을 참고

<br>

스프링 설정 변경

`SpringConfig` 파일 내의 설정 변경

```java
@Configuration
public class SpringConfig {

    private DataSource dataSource;

    @Autowired
    public SpringConfig(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        return new JdbcMemberRepository(dataSource);
    }
}
```

- `DataSource`는 데이터베이스 커넥션을 획득할 때 사용하는 객체이다.
- 스프링 부트는 데이터베이스 커넥션 정보를 바탕으로 DataSource를 생성하고 스프링 빈으로 만들어둔다. 이를 바탕으로 DI를 받을 수 있다.

<br>

##### 스프링 부트의 특징

- OCP (Open-Closed Principle). 개방-폐쇄 원칙
  - 확장에는 열려있고, 수정 및 변경에는 닫혀있다.
- **DI, 의존성 주입을 사용하면 기존 코드는 전혀 수정하지 않고, 설정만으로 구현 클래스를 변경할 수 있다.**

<br>

#### 6-3. 스프링 통합 테스트

스프링 컨테이너와 DB까지 연결한 통합 테스트 (↔ 단위 테스트. 스프링 컨테이너 & DB 연동 없이 프로젝트 단위별로 테스트를 진행하는 것)

##### 회원 서비스 스프링 통합 테스트

```java
@SpringBootTest
@Transactional

class MemberServiceIntegrationTest {

    @Autowired MemberService memberService;
    @Autowired MemberRepository memberRepository;
	
    @Test
    public void 회원가입() {
        ...
    }
    
    @Test
    public void 중복_회원_예외() {
        ...
    }
}
```

- `@SpringBootTest` : 스프링 컨테이너와 함께 테스트를 실행함
- `@Transactional` : 테스트 시작 전 트랜잭션을 시작하고, 테스트 완료 후 항상 콜백함
  - DB에 데이터가 남지 않으므로 다음 테스트에 영향을 주지 않는다.

<br>

#### 6-4. 스프링 JdbcTemplate

- 설정은 순수 Jdbc와 동일함 (build.gradle 파일 내에 dependencies)
  - `implementation 'org.springframework.boot:spring-boot-starter-jdbc'`

- `JdbcTemplate`, `MyBatis` 와 같은 라이브러리는 JDBC API의 반복 코드를 대부분 제거해준다. 하지만 SQL을 직접 작성해야 한다.

<br>

##### 스프링 JdbcTemplate 회원 리포지토리

- 마찬가지로 코드는 `JdbcTemplateMemberRepository` 클래스 파일을 참고할 것

<br>

##### JdbcTemplate 사용 가능하도록 스프링 설정 변경

- `SpringConfig` 코드 변경

```java
@Bean
public MemberRepository memberRepository() {
    //        return new MemoryMemberRepository();
    //        return new JdbcMemberRepository(dataSource);
    return new JdbcTemplateMemberRepository(dataSource);
}
```

<br>

#### 6-5. JPA

※ JPA는 별도로 추가 공부할 예정임

- 기존의 반복 코드 + 기본적인 SQL을 직접 만들어서 실행해준다.
- SQL과 데이터 중심의 설계 → 객체 중심의 설계로 패러다임 전환 가능
- 개발 생산성을 크게 높일 수 있음

<br>

##### JPA 라이브러리 추기

- `build.gradle` 파일에 JPA, H2 DB 관련 라이브러리 추가
  - `spring-boot-starter-data-jpa` 내부에 jdbc 관련 라이브러리를 포함함

```java
implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
runtimeOnly 'com.h2database:h2'
```

<br>

##### 스프링 부트에 JPA 설정 추가

- `application.properties` 파일 수정
  - `show-sql` : JPA가 생성하는 SQL을 출력
  - `ddl-auto` : JPA는 테이블을 자동으로 생성하는 기능을 제공
    - `none` : 해당 기능을 Off
    - `create` : Entity 정보를 바탕으로 테이블을 직접 생성해줌

```java
spring.jpa.show-sql=true
spring.jpa.hibernate.ddl-auto=none
```

<br>

##### JPA 엔티티 매핑

```java
package hello.hellospring.domain;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Member {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

<br>

##### JPA 회원 리포지토리

- JPA에는 `EntityManager` 가 필요함.
- 기본적인 Query문은 `.persist`, `.find` 와 같은 문법으로 사용 가능
  - 복잡한 Query문은 JPQL 문법을 사용해야함

```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import javax.persistence.EntityManager;
import java.util.List;
import java.util.Optional;

public class JpaMemberRepository implements MemberRepository {

    private final EntityManager em;

    public JpaMemberRepository(EntityManager em) {
        this.em = em;
    }

    @Override
    public Member save(Member member) {
        em.persist(member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        Member member = em.find(Member.class, id);
        return Optional.ofNullable(member);
    }

    @Override
    public Optional<Member> findByName(String name) {
        List<Member> result = em.createQuery("select m from Member m where m.name = :name", Member.class)
                .setParameter("name", name)
                .getResultList();
        return result.stream().findAny();
    }

    @Override
    public List<Member> findAll() {
        return em.createQuery("select m from Member m", Member.class)
                .getResultList();
    }
}
```

<br>

##### 서비스 계층에 트랜잭션 추가

```java
import org.springframework.transaction.annotation.Transactional;

@Transactional
public class MemberService {}
```

- 스프링은 해당 클래스의 메서드를 실행할 때 트랜잭션을 시작하고, 메서드가 정상적으로 종료되면 트랜잭션을 커밋한다. 런타임 예외가 발생하면 롤백한다.
- **JPA를 통한 모든 데이터 변경은 트랜잭션 안에서 실행되어야 한다.!!**

<br>

##### JPA를 사용하도록 스프링 설정 변경

- `SpringConfig` 파일 수정

```java
@Configuration
public class SpringConfig {

//    private DataSource dataSource;
    private final EntityManager em;
    
//    @Autowired
//    public SpringConfig(DataSource dataSource) {
//        this.dataSource = dataSource;
//    }
    
    public SpringConfig(EntityManager em) {
        this.em = em;
    }

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
//        return new MemoryMemberRepository();
//        return new JdbcMemberRepository(dataSource);
//        return new JdbcTemplateMemberRepository(dataSource);
        return new JpaMemberRepository(em);
    }
}
```

<br>

#### 6-6. 스프링 데이터 JPA

스프링 부트 + JPA를 활용하면 개발 생산성이 많이 증가하고, 개발해야 할 코드의 양도 확연이 줄어듬

++ 스프링 데이터 JPA를 사용하면, 리포지토리를 구현클래스가 아닌 인터페이스만 생성하여 개발을 할 수 있다.

반복 개발하는 기본적인 CRUD 기능이 제공됨.. (대애박..)

스프링 데이터 JPA 설정은 기존 JPA 설정을 그대로 따라감

<br>

##### 스프링 데이터 JPA 회원 리포지토리

- 구현 클래스가 아닌 인터페이스로 생성
- 인터페이스가 인터페이스를 불러오기 때문에 `extends` 사용

```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface SpringDataJpaMemberRepository extends JpaRepository<Member, Long>, MemberRepository {
    
    Optional<Member> findByName(String name);
}

```

<br>

##### 스프링 데이터 JPA 회원 리포지토리를 사용하도록 스프링 설정 변경

- `SpringConfig` 파일 수정

```java
@Configuration
public class SpringConfig {

    private final MemberRepository memberRepository;
    
    public SpringConfig(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository);
    }
}
```

- 스프링 데이터 JPA가 `SpringDataJpaMemberRepository`를 스프링 빈으로 자동 등록함

<br>

##### 스프링 데이터 JPA 제공 기능

- 인터페이스를 통한 기본적인 CRUD
- 메소드 이름을 구성하여 조회 기능 제공이 가능하다
  - `findByName()`
  - `findByEmail()`
- 페이징 기능 자동 제공

<br>

***

### 7. AOP

#### AOP가 필요한 상황

- 모든 메소드의 호출 시간을 측정하고 싶을 경우
  - 회원 가입, 회원 조회 시간이 알고 싶을 때!!
- 공통 관심 사항(cross-cutting concern) vs. 핵심 관심 사항(core concern)
  - 시간 측정 로직은 공통 관심 사항
  - 이 로직을 핵심 비즈니스 로직과 섞으면, 유지보수가 어려움
  - 별도의 공통 로직을 만들어 관리하자

<br>

#### AOP 적용

- 공통 관심사항과 핵심 관심 사항을 분리

![image-20220110223229530](spring_스프링입문.assets/image-20220110223229530.png)

##### 시간 측정 AOP 등록

- `aop` 패키지 생성 - `TimeTraceAop` 클래스 파일 생성

```java
package hello.hellospring.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Component
@Aspect
public class TimeTraceAop {
    @Around("execution(* hello.hellospring..*(..))")
    public Object execute(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        System.out.println("START: " + joinPoint.toString());

        try {
            return joinPoint.proceed();
        } finally {
            long finish = System.currentTimeMillis();
            long timeMs = finish - start;
            System.out.println("END: " + joinPoint.toString() + " " + timeMs + "ms");
        }
    }
}
```

<br>

#### 스프링 AOP 동작 방식

##### AOP 적용 전 의존관계

<img src="spring_스프링입문.assets/image-20220110223448323.png" alt="image-20220110223448323" style="zoom:67%;" />

##### AOP 적용 후 의존관계

<img src="spring_스프링입문.assets/image-20220110223512260.png" alt="image-20220110223512260" style="zoom:67%;" />

<br>

##### AOP 적용 전 전체 그림

<img src="spring_스프링입문.assets/image-20220110223536201.png" alt="image-20220110223536201" style="zoom:67%;" />

##### AOP 적용 후 전체 그림

<img src="spring_스프링입문.assets/image-20220110223553618.png" alt="image-20220110223553618" style="zoom:67%;" />

<br>

***

#### 참고 자료

[스프링 입문 - 코드로 배우는 스프링 부트, 웹 MVC, DB 접근 기술](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EC%9E%85%EB%AC%B8-%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8/dashboard)

본 README 파일은 김영한님의 **스프링 입문 - 코드로 배우는 스프링 부트, 웹 MVC, DB 접근 기술** 강의 및 강의 자료를 정리한 파일이다.

<br>

<br>

***

✨ 자바 기초 문법을 약 10일 간 공부하고,  3일동안 짧게 웹 개발을 위한 프레임워크인 Spring (Boot)를 공부하였다. 방대한 내용을 단 3일만에 이해한다고 할 수 없지만, 기본적인 프로젝트 설정, 웹 MVC, DI, DB 연동, JPA, 테스트, AOP 등의 개념과 관련 용어들을 한 번씩 듣고 모르면 구글에서 찾아보는 시간이 매우 유익했다고 생각한다. 계속해서 열심히 공부하자! 2022.01.10

