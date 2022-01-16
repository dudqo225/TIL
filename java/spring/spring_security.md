# Spring | Security

## 1. Spring Security

### Spring Security 란

- Spring 기반의 애플리케이션 보안(인증, 권한, 인가 등)을 담당하는 스프링의 하위 프레임워크
- 유저에 대한 인증 및 권한에 대한 부분을 Filter 흐름에 따라 처리함
- 보안과 관련한 많은 옵션을 제공하기 때문에 개발자 입장에서 일일이 보안 관련 로직을 작성하지 않아도 된다는 장점이 있음

<br>

#### 용어 정리

- ##### Principal (접근 주체) 

  - 접근하는 대상 (User)

- ##### Authentication (인증) 

  - 리소스에 접근한 User가 누구인지 식별. 'A'라고 주장하는 접근 주체가 'A'가 맞는지 확인하는 것

- ##### Authorization (인가, 권한) 

  - 접근한 User가 리소스에 대한 접근 권한이 있는지 검사
  - 프로세스 상 **먼저 신분 인증(Authentication)**을 거치고, 서버 자원에 **접근할 권한이 있는지를 확인**한다.

- ##### Credential (증명서)

  - 인증 과정 중, 접근 주체가 본인임을 인증하기 위해 서버에 제공하는 것 (ID, PW 등)

<br>

![img](spring_security.assets/img.png)

<br>

#### 기본 구조 - Filter Chain

스프링 시큐리티의 기본 구조는 **Filter Chain** 구조이다. 사용자의 정보가 여러개로 연결(Chaining)된 Filter를 거친다. 

예를 들어, OAuth 2.0 인증을 시도하려고 할때는 `UsernamePasswordAuthenticationFilter` 는 OAuth 2.0 인증을 실시할 수 없으므로 이 필터는 건너뛰고 다음 필터로 넘어가게 된다. 이후, `OAuth2ClientAuthenticationProcessingFilter` 에서 OAuth 2.0을 이용한 인증을 진행한다. 

여러개의 Filter 들을(**AuthenticationFilter**) 거치면서 인증을 진행하고 앞선 Filter에서 인증이 완료되면 '인증된 사용자' 즉, **인증된 요청으로 처리**된다. 모든 Filter를 거치고도 인증이 완료되지 않으면 User의 요청은 인증되지 않은 요청이 된다.

<br>

#### AuthenticationFilter

- 스프링 시큐리티는 보안과 관련된 여러개의 필터 리스트를 가지고 있음

- `springSecurityFilterChain` → 필터 리스트를 가지고 있는 객체

- **AuthenticationFilter** 리스트

  1. `WebAsyncManagerIntegrationFilter`
     - SpringsecurityContextHolder는 **ThreadLocal**(하나의 쓰레드에서 SecurityContext를 공유하는 방식) 기반으로 동작함. 비동기(Async) 관련 기능을 쓸 때에도 Securitycontext를 사용할 수 있도록 만들어주는 필터

  2. `SecurityContextPersistenceFilter`
     - SecurityContext가 없으면 만들어주는 필터이다.
     - SecurityContext : Authentication 객체를 보관하는 보관 인터페이스
  3. `HeaderWriterFilter`
     - 응답(Response)에 security와 관련된 헤더 값을 설정하는 필터
  4. `CsrfFilter`
     - CSRF 공격을 방어하는 필터
     - CSRF : Cross-Site Request Forgery. 사이트 간 요청 위조. 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 해서 특정 웹페이지를 보완에 취약하게 하거나 수정, 삭제하는 작업을 하게 만드는 공격 기법
  5. `LogoutFilter`
     - 로그아웃 요청을 처리하는 필터
     - DefaultLogoutPageGeneratingFilter가 로그아웃 기본페이지를 생성
  6. `UsernamePasswordAuthenticationFilter`
     - username, password를 사용하는 form 기반 인증 처리 필터
     - AuthenticationManager를 통해 인증 실행
       - 성공하면, Authentication 객체를 SecurityContext에 저장하고 AuthenticationSuccessHandler 실행
       - 실패하면, AuthenticationFailureHandler 실행
  7. `RequestCacheAwareFilter`
     - 인증 후, 원래의 Request 정보로 재구성하는 필터
  8. `SecurityContextHolderAwareRequestFilter`
  9. `AnonymousAthenticationFilter`
     - 이 필터 순서에 올때까지 앞에서 사용자 정보의 인증이 완료되지 않으면, 해당 요청은 익명의 사용자가 보낸 것으로 판단하고 처리함
     - Authentication 객체를 새로 생성한다(AnonymousAuthenticationToken)
  10. `SessionManagementFilter`
      - 세션 변조 공격 방지 (Session ID를 계속 다르게 바꿔서 클라이언트에 보내줌)
      - 유효하지 않은 세션으로 접근하면 URL 핸들링
      - 하나의 Session ID로 접속하는 최대 세션 수 설정
      - 세션 생성 전략 설정
  11. `ExceptionTranslationFilter`
      - 앞선 필터 처리 과정에서 인증 예외(AuthenticationException) 또는 인가 예외(AccessDeniedException)가 발생한 경우, 해당 예외를 캐치해서 처리하는 필터
      - 모든 예외를 처리하는 것은 아님
  12. `FilterSecurityInterceptor`
      - 인가(Authorization)을 결정하는 AccessDecisionManager에게 접근 권한이 있는지 확인하고 처리하는 필터

<br>

## 2. JWT & Spring Security 실습











### 참고 자료

https://pozafly.github.io/tripllo/(4)spring-security-jwt/

https://jeong-pro.tistory.com/205

https://www.bottlehs.com/springboot/%EC%8A%A4%ED%94%84%EB%A7%81-%EB%B6%80%ED%8A%B8-spring-security%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%9D%B8%EC%A6%9D-%EB%B0%8F-%EA%B6%8C%ED%95%9C%EB%B6%80%EC%97%AC/

https://bcp0109.tistory.com/301

https://mia-dahae.tistory.com/121