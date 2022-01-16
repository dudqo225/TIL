

# Spring | JWT + Spring Security

사용자 인증 관련  JWT 토큰과 스프링 프레임워크의 Spring Security를 공부하고 관련된 내용을 정리한 글

<br>

##  목차

> 1. [JWT](#1-JWT)
>    1. [JWT란?](#JWT란?)
>    2. [장단점](#장단점)
>    3. [JWT 구성요소](#JWT-구성요소)
>    4. [토큰 인증 타입](#토큰-인증-타입)
>    5. [Refresh Token](#Refresh-Token)
>    6. [Refresh Token 저장소](#Refresh-Token-저장소)
> 2. [Spring Security](#2-Spring-Security)
>    1. [JWT & Security 관련 의존성 추가](#JWT-&-Security-관련-의존성-추가)
>    2. [사용자 (Member) 도메인 설계](#사용자-(Member)-도메인-설계)

<br>

***

## 1. JWT

#### JWT란?

- **J**son **W**eb **T**oken
- Json 객체를 이용해서 토큰 자체에 정보를 저장하는 Web Token이다. 쿠키 or 세션을 이용한 인증보다 안전하면서 효율적임
- 구성
  - Header
  - Payload
  - Signature
- `Authorization: <type> <credentials>` 형태로 Request Header에 담겨서 전달된다.

<br>

#### 장단점

##### 장점

- 중앙 인증 서버와 저장소에 대한 의존성이 없어서 수평 확장에 유리함
- Base64 URL Safe Encoding 으로, URL, Cookie, Header 등 어떠한 형태로도 사용이 가능함
- Stateless 한 서버 구현이 가능함
- 웹 + 모바일에서도 사용 가능
- 인증 정보를 다른 곳에서도 사용 가능함 (OAuth)

<br>

##### 단점

- Payload의 정보가 많아지면 네트워크 사용량이 증가함
- 타인이 토큰을 Decode 하여 데이터 확인이 가능하다
- 토큰을 탈취당한 경우 대응이 어렵다
  - 서버에서 관리하는 것이 아니기 때문에 토큰을 탈취당한 경우 강제 로그아웃 처리가 불가능
  - 토큰의 유효시간이 만료되기 전까지 탈취자가 자유롭게 인증이 가능함
  - 위 문제 발생 방지를 위해서 토큰의 유효시간을 짧게 하고, refresh token을 발급하는 방식을 사용한다.

<br>

#### JWT 구성요소

##### Header

- `alg` : Signature를 해싱(Hashing)하기 위한 알고리즘 정보를 가지고 있음
- `typ` : 토큰의 타입을 나타냄. 기본적으로 JWT를 사용

#####  Payload

- 서버 - 클라이언트가 주고받는 실제 정보에 대한 내용을 담고 있음
- JWT가 기본적으로 가지고 있는 키워드가 있다(https://datatracker.ietf.org/doc/html/rfc7519#section-4.1)
- 추가도 가능
  - `iss` : 토큰 발급자
  - `sub` : 토큰 제목
  - `aud` : 토큰 대상
  - `exp` : 토큰 만료시간
  - `nbf` : Not Before
  - `iat` : 토큰 발급시간
  - `jti` : JWT 고유 식별자

##### Signature

- 서버에서 토큰의 유효성을 검증하기 위한 문자열
- Header + Payload + Secret Key 로 토큰 값을 생성하므로 데이터 변조 여부 판단 가능
- Secret Key가 노출되지 않도록 서버에서 잘 관리해야 함

<br>

#### 토큰 인증 타입

`Authorization: <type> <credentials>` 중에서 `<type>` 부분에 들어갈 값.

별도의 규칙이 있다기 보다는, 일반적(관습적)으로 많이 사용하는 형태임

- Basic : 사용자 아이디 & 암호를 Base64 로 인코딩한 값을 토큰으로 사용
- Bearer : JWT or OAuth 에 대한 토큰을 사용
- Digest
  - 서버에서 난수 데이터 문자열을 클라이언트에 보냄
  - 클라이언트는 사용자 정보 + nonce를 포함하는 해시값을 통해서 응답
- HOBA : 전자 서명 기반 인증
- Mutual : 암호를 이용한 클라이언트 - 서버 상호 인증
- AWS44-HMAC-SHA256 : AWS 전자 서명 기반 인증

<br>

#### Refresh Token

JWT가 탈취되면 누구나 이 토큰을 활용하여 API를 호출할 수 있다는 단점이 있다.

세션이 탈취되면 세션 저장소에서 세션 ID를 삭제하는 방법으로 문제를 해결할 수 있지만, JWT는 서버에서 관리하지 않기 때문에 이러한 탈취에 대응하기가 어렵다.

이러한 문제 발생을 방지하기 위해서, 또 토큰이 혹시 탈취되더라도 피해를 최소화하기 위해서 토큰의 유효시간을 짧게 할 수 있다. 그러나, 토큰의 유효시간을 30분으로 설정하면 사용자는 매 30분마다 새로 로그인을 해서 토큰을 발급받아야 한다.

사용자가 매번 새로 **로그인하는 과정을 생략**하기 위해 필요한 것이 바로 Refresh Token 이다.

<br>

Refresh Token은 Access Token(로그인 토큰)보다 유효시간이 길다.

만일 Access Token이 만료된 사용자가 재발급을 원할 경우 Refresh Token을 전달한다. 서버는 Access Token에 담긴 사용자의 정보를 확인하고 Refresh Token이 아직 만료되지 않았으면 새로운 토큰을 발급해준다. 이를 통해 사용자는 매번 로그인을 해야하는 과정없이 서비스를 이용할 수 있다.

Refresh Token은 사용자가 로그인할 때 같이 발급되고 클라이언트 측에서 안전하게 보관해야 한다. Access Token은 클라이언트 - 서버 통신때마다 주고 받기 때문에 탈취 위험이 크지만, Refresh Token은 매 요청마다 주고받지 않아 탈취 위험이 적다. 

<br>

#### Refresh Token 저장소

- Refresh Token 은 서버에서 별도 저장소에 보관하는 것이 좋음
- Token에 사용자 정보가 없기 때문에 저장소에 값이 있으면 검증시 어떤 사용자의 토큰인지 판단하기 쉬움
- 토큰을 탈취당했을 때 저장소에서 Refresh Token 정보를 삭제하면, Access Token 만료 후 재발급이 안되도록 강제 로그아웃 처리가 가능함
- 일반적으로 Redis를 많이 사용한다.
  - Redis : 키-값 구조의 비정현 데이터를 저장/관리하기 위한 오픈 소스 기반의 비관계형 데이터베이스 관리 시스템

<br>

***

## 2. Spring Security

Spring Security는 사용자 정보(ID/PW) 검증 및 유저 정보 관리를 쉽게 할 수 있도록 도움

스프링 시큐리티는 JWT와 많이 결합되어서 사용되지만, 기본적으로는 세션 기반 인증을 사용한다.

<br>

### JWT & Security 관련 의존성 추가

- Gradle 파일에 JWT와 Security 관련 의존성(Dependencies) 추가

```java
// build.gradle
...
    
dependencies {
    
	...
        
    // security 관련 의존성
    implementation 'org.springframework.boot:spring-boot-starter-security'

    // jwt 관련 의존성
    compile group: 'io.jsonwebtoken', name: 'jjwt-api', version: '0.11.2'
    runtime group: 'io.jsonwebtoken', name: 'jjwt-impl', version: '0.11.2'
    runtime group: 'io.jsonwebtoken', name: 'jjwt-jackson', version: '0.11.2'
        
    ...
}
```

<br>

### 사용자 (Member) 도메인 설계

#### Member 도메인

- Member Entity
- MemberRepository
- MemberService
- MemberController
- application.yml - DB와 JWT Secret Key 설정

<br>

##### Member Entity

```java
@Getter
@NoArgsConstructor
@Table(name = "member")
@Entity
public class Member {

    @Id
    @Column(name = "member_id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String email;

    private String password;

    @Enumerated(EnumType.STRING)
    private Authority authority;

    @Builder
    public Member(String email, String password, Authority authority) {
        this.email = email;
        this.password = password;
        this.authority = authority;
    }
}
```

- 권한은 Enum 클래스로 생성

```java
public enum Authority {
    ROLE_USER, ROLE_ADMIN
}
```

<br>

##### MemberRepository

```java
@Repository
public interface MemberRepository extends JpaRepository<Member, Long> {
    Optional<Member> findByEmail(String email);
    boolean existsByEmail(String email);
}
```

- `findByEmail` : email을 기준으로 Member를 찾는 쿼리
- `existsByEmail` : 중복 가입 방지를 위한 boolean을 반환하는 쿼리

<br>

##### MemberService

```java
@Service
@RequiredArgsConstructor
public class MemberService {
    private final MemberRepository memberRepository;

    @Transactional(readOnly = true)
    public MemberResponseDto getMemberInfo(String email) {
        return memberRepository.findByEmail(email)
                .map(MemberResponseDto::of)
                .orElseThrow(() -> new RuntimeException("유저 정보가 없습니다."));
    }

    // 현재 SecurityContext 에 있는 유저 정보 가져오기
    @Transactional(readOnly = true)
    public MemberResponseDto getMyInfo() {
        return memberRepository.findById(SecurityUtil.getCurrentMemberId())
                .map(MemberResponseDto::of)
                .orElseThrow(() -> new RuntimeException("로그인 유저 정보가 없습니다."));
    }
}
```

- `SecurityUtil.getCurrentMemberId()` : 나의 정보를 가져올 때 사용
- API 요청이 들어오면 Access Token을 복호화해서 유저 정보를 꺼내고 `SecurityContext` 에 저장
- `SecurityContext` 에 저장된 유저 정보는 전역(global)으로 어디서든 꺼낼 수 있음
- `SecurityUtil` 클래스에는 유저 정보 중 Member ID만 반환하는 메소드가 정의되어 있음

<br>

##### MemberController

```java
@RestController
@RequiredArgsConstructor
@RequestMapping("/member")
public class MemberController {
    private final MemberService memberService;

    @GetMapping("/me")
    public ResponseEntity<MemberResponseDto> getMyMemberInfo() {
        return ResponseEntity.ok(memberService.getMyInfo());
    }

    @GetMapping("/{email}")
    public ResponseEntity<MemberResponseDto> getMemberInfo(@PathVariable String email) {
        return ResponseEntity.ok(memberService.getMemberInfo(email));
    }
}
```

<br>

##### application.yml

- yml 파일 내에 JWT Secret Key 저장
- 원래는 github 같은 원격 저장소에 올라가지 않도록 별도로 보관하는 것이 안전하다.

<br>

##### 참고

https://bcp0109.tistory.com/301

