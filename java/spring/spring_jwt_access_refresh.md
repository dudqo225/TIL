# Spring | JWT - Access & Refresh Token 1

<br>

### 목차

> 1. Access & Refresh Token 생성
> 2. Token 유효성 검증
> 3. JWT Filter 적용
> 4. @AuthenticationPrincipal
> 5. 401 & 403 

<br>

프로젝트에서 **소셜 로그인**을 적용하면서 토큰 기반의 인증 방식을 사용하고 있다. 

예를 들어 **OAuth**를 활용한 카카오 API를 사용하면 카카오에서 생성된 Access Token과 Refresh Token을 받아올 수 있지만, 보안상의 이슈로 우리 서비스의 백엔드 서버 자체에서 토큰을 생성하기로 결정하였다.

<br>

## 1. Access & Refresh Token 생성

<br>

### TokenProvider Class

##### 1. 토큰 생성을 위한 초기 셋팅

```java
@Component
@RequiredArgsConstructor
public class TokenProvider {

    @Value("${jwt.secret}")
    private String secretKey;

    private final long ACCESS_TOKEN_VALID_TIME = 30 * 60 * 1000L;   // 30분
    private final long REFRESH_TOKEN_VALID_TIME = 60 * 60 * 24 * 7 * 2000L;   // 2주
    
    // 의존성 주입 이후 초기화를 수행하는 어노테이션
    @PostConstruct
    protected void init() {
        secretKey = Base64.getEncoder().encodeToString(secretKey.getBytes());
    }

    ...
      
}
```

- `jwt` 에 사용되는 **secretKey**도 보안상 유출될 수 있기때문에, 소스코드 내에 직접 작성하지 않고 프로젝트 `.yml` 혹은 `.properties` 파일에 작성한다.
  - 이후 소스코드 안에서 `@Value` 어노테이션으로 연결해준다.
- access token과 refresh token의 유효기간을 설정한다.
  - 일반적으로 `access token`은 30분, `refresh token`은 1~2주 내외로 설정한다고 한다.
- `init()` 메서드로 의존성 주입 후 초기화를 수행한다.

<br>

##### 2. 토큰 생성

```java
// Access Token 생성

public String createJwtAccessToken(String userId, List<String> roles) {
  Claims claims = Jwts.claims().setSubject(userId);
  claims.put("roles", roles);
  Date now = new Date();
  Date expiration = new Date(now.getTime() + ACCESS_TOKEN_VALID_TIME);

  return Jwts.builder()
    .setClaims(claims) // 정보 저장
    .setIssuedAt(now) // 토큰 발행시간 정보
    .setExpiration(expiration) // 토큰 만료시간 정보
    .signWith(SignatureAlgorithm.HS256, secretKey) // 암호화 알고리즘
    .compact();
}
```

- `Access Token`
  - 사용자 정보를 식별할 수 있는 **userId**
  - 권한 검증을 위한 **roles**
  - 발행시간, 만료시간(**Expiration**) 정보
  - **HS256** 암호화 알고리즘을 적용한다.

<br>

```java
// Refresh Token 생성

public String createJwtRefreshToken(String value) {
  Claims claims = Jwts.claims();
  claims.put("value", value);
  Date now = new Date();
  Date expiration = new Date(now.getTime() + REFRESH_TOKEN_VALID_TIME);

  return Jwts.builder()
    .setClaims(claims)
    .setIssuedAt(now)
    .setExpiration(expiration)
    .signWith(SignatureAlgorithm.HS256, secretKey)
    .compact();
}
```

- `Refresh Token`
  - 식별 정보 **value**
  - 발행시간, 만료시간(**Expiration**) 정보
  - **HS256** 암호화 알고리즘을 적용한다.

<br>

## 2. Token 유효성 검증

<br>

