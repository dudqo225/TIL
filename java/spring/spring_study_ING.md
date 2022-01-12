# Spring | 공부하면서 정리하기



## DataBase

### Sub PJT 1 - ERD

![image-20220112212049081](C:\Users\YB\AppData\Roaming\Typora\typora-user-images\image-20220112212049081.png)

<br>

***

### JPA

### Entity 구현

- User
- Conference
- UserConference
- ConferenceCategory
- ConferenceHistory

<br>

##### @Setter 와 @Builder

Lombok 라이브러리를 활용하면 `@Getter`, `@Setter`, `@Builder` 등의 Annotation을 사용해서 쉽게 만들 수 있다. 또한 매개변수가 없는 기본 생성자나 선언된 모든 필드를 매개변수로 갖는 생성자를 쉽게 만들 수 있다(`@NoArgsConstructor`, `@AllArgsConstructor`).

이 중에서 `@Setter` 를 무분별하게 사용하면 여러 곳에서 객체의 값을 변경할 수 있기 때문에 객체의 일관성을 보장할 수 없다. 유지보수성을 높이기 위해 Setter의 사용을 지양할 필요가 있다.

대신 `@Builder` 어노테이션을 사용하여 개발 편의성을 높일 수 있다.

```java
// @Builder 패턴 사용 예시
User user = User.builder()
    	.userId(userRegisterInfo.getUserId())
    	.password(passwordEncoder.encode(userRegisterInfo.getPassword()))
    	.position(userRegisterInfo.getPosition())
    	.department(userRegisterInfo.getDepartment())
    	.name(userRegisterInfo.getName())
    	.build();
...
```

<br>

##### @ManyToOne

- 테이블 간 1:N 설정을 하기 위한 어노테이션이다. M(다) 에 해당하는 객체(Entity)에 작성해야 한다. 
- `@JoinColumn=(name="컬럼명")` 으로 연결되는 테이블의 FK 컬럼 이름을 설정할 수 있다.
- `@OnDelete(action=OnDeleteAction.CASCADE)`
  - 1:N 관계에서 1에 해당하는 테이블의 특정 레코드가 삭제되면, 해당 레코드와 관련있는 모든 M 테이블의 레코드가 삭제되도록 설정하는 어노테이션
  - ex. 유저(1) - 컨퍼런스(N)
    - 유저 한 명은 여러 개의 컨퍼런스를 생성할 수 있다.
    - 만약 유저 레코드가 삭제되면, 해당 유저가 만든 모든 컨퍼런스 레코드가 자동으로 DB에서 삭제된다.
- 참고
  - https://yonguri.tistory.com/69
  - https://cheese10yun.github.io/lombok/
  - https://github.com/cheese10yun/spring-jpa-best-practices/blob/master/doc/step-06.md
  - https://tomining.tistory.com/180
  - https://ppomelo.tistory.com/155
  - https://blog.jiniworld.me/139
  - https://velog.io/@aidenshin/%EB%82%B4%EA%B0%80-%EC%83%9D%EA%B0%81%ED%95%98%EB%8A%94-JPA-%EC%97%94%ED%8B%B0%ED%8B%B0-%EC%9E%91%EC%84%B1-%EC%9B%90%EC%B9%99
  - https://kukekyakya.tistory.com/m/546
  - https://velog.io/@devsh/JPA-CASCADE-%EC%98%81%EC%86%8D%EC%84%B1-%EC%A0%84%EC%9D%B4
  - https://velog.io/@max9106/JPA%EC%97%94%ED%8B%B0%ED%8B%B0-%EC%83%81%ED%83%9C-Cascade
  - https://minkukjo.github.io/framework/2020/04/28/Spring-107/
  - https://data-make.tistory.com/614

<br>

### Repository 구현

- Entity(객체)에 관련하여 만들어진 데이터베이스에 접근하는 여러 메스드를 사용하기 위한 인터페이스
- 데이터를 불러오거나 저장, 수정, 삭제 등 CRUD 에 대해서 정의하는 계층이다.
- `JpaRepository` 를 상속받아서 간단하고 쉽게 데이터 조작을 할 수 있다.
  - JpaRepository는 인터페이스로, 미리 데이터 검색에 관한 메소드가 정의되어 있다.
  - `JpaRepository<대상 엔티티, 해당 엔티티의 PK타입>`
  - `@Repository` 어노테이션을 붙여서 JpaRepository임을 명시한다.
  - *JPA 에 대해서는 공부할 양이 상당히 많기 때문에 계속해서 심화 학습이 필요하다.*

```java
// UserRepository
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    // User 정보 Update
    @Modifying(clearAutomatically = true)
    @Transactional
    @Query(value = "update user set department = :department, position = :position, name = :name where user_id = :userId", nativeQuery=true)    
    int updateUserInfo(@Param("department") String department, @Param("position") String position, @Param("name") String name, @Param("userId") String userId);
    
    // User 정보 삭제
    @Modifying(clearAutomatically = true)
    @Transactional
    @Query(value = "delete from user where user_id = :userId", nativeQuery=true)    
    int deleteUserInfo(@Param("userId") String userId);
 	
    ...
}
```

- `@Query` 
  - JpaRepository에서 제공하는 기본 메서드나, 메서드 네이밍을 통해서 원하는 쿼리를 실행할 수 있다.
  - 하지만 좀 더 복잡한 쿼리가 필요하다면 쿼리를 직접 작성해야 하는데, 이 때 붙이는 어노테이션이 @Query이다.
  - 기본적으로 JPQL 문법으로 작성할 수 있고, `nativeQuery=true` 옵션을 사용하면 일반적인 SQL 형식으로 작성할 수 있다.
- `@Modifying`
  - 데이터에 변경이 일어나는 INSERT, UPDATE, DELETE, DDL 등에 관련된 퀴리를 작성할 때 사용한다.
  - @Query에 벌크 연산 쿼리(다건의 수정, 삭제 연산을 하나의 쿼리로 작성하는 것)을 작성하고 `@Modifying`을 붙이지 않으면, **InvaidDataAccessApiUsage Exception** 이 발생한다.
  - JPA Entity LifeCycle을 무시하고 쿼리가 실행되므로 영속성 관리에 주의해야 한다.
    - `clearAutomatically=true` 속성이 붙어있으면, 쿼리 메서드 실행 직후, **영속성 컨텍스트**를 clear한다.

##### 영속성 컨텍스트

- JPA에서 데이터를 조회하면 1차 캐시를 확인하고, 해당 엔티티가 1차 캐시에 존재하면 DB에 접근하지 않고 1차 캐시에 있는 엔티티를 반환한다. **1차 캐시를 활용**하면 DB에 접근하는 횟수를 줄일 수 있기 때문에 **성능을 개선**할 수 있다는 장점이 있다.
- 하지만 **벌크 연산 쿼리**를 실행할 경우 1차 캐시로 인해 오히려 예측하지 못한 결과가 나올 수 있다. 벌크 연산은 1차 캐시와 같은 **영속성 컨텍스트를 무시하고 쿼리를 실행**하기 때문에 쿼리 실행 후 데이터가 변경되면 1차 캐시와 DB의 데이터 싱크가 맞지 않을 수 있다. `@Modifying` 어노테이션의 `clearAutomatically` 속성을 `true` 로 적용하여 쿼리 실행 후 영속성 컨텍스트를 clear해서 데이터 동기화 문제를 방지할 수 있다.

<br>

- `@Transactional`
  - 트랜잭션이란, DB의 상태를 변경하는 작업 or 한번에 수행되어야 하는 연산들을 말한다.
  - 스프링에서는 메소드, 클래스, 인터페이스 위에 간단하게 @Transactional 어노테이션을 붙여서 트랜잭션임을 명시할 수 있다.
- 참고
  - https://whitepro.tistory.com/265
  - https://velog.io/@kdhyo/JavaTransactional-Annotation-%EC%95%8C%EA%B3%A0-%EC%93%B0%EC%9E%90-26her30h
  - https://araikuma.tistory.com/329
  - https://devhyogeon.tistory.com/4

<br>

***

## API

### 공통

- API Model
  - Request
  - Response
- Service & Service Implementation
- Controller
- Swagger

<br>

#### API Model

<br>

#### Service & Service Implementation

MVC 패턴에서 비즈니스 로직을 담당하는 Service는 인터페이스로, Service Implementation은 Service 인터페이스를 확장한 클래스로 작성한다.

Controller에서는 클라이언트에서 받은 요청(request)을 통해서 Request 관련 객체를 매개변수로 받고, 이를 이용하여 Service와 Service를 확장한 ServiceImpl의 메서드를 호출한다. 이 메서드를 통해 DB 데이터에 접근 가능한 Repository를 호출하고 이에 따른 응답(response)을 담아 View에 전달한다.

비즈니스 로직을 담당하는 모델은 상황에 따라서 언제든지 변할 수 있기 때문에 이러한 변화에 대응하기 위해서 확장을 염두에 둔 인터페이스 형태로 **Service**를 구성한다. **인터페이스**는 타입에 **어떤 구현 객체를 넣는지에 따라서 실행결과가 달라질** 수 있도록 하는 기술이다. 구현 객체를 하나 만들고(ServiceImpl), 비즈니스 로직이 다른 기능을 또 추가해야 할 경우 객체를 하나 더 만들어(ServiceImpl2) 사용하면 된다. 코드의 확장성과 재사용성이 커지고 유지보수를 쉽게할 수 있는 것이다.

```java
// User Service 인터페이스
public interface UserService {
	User createUser(UserRegisterPostReq userRegisterInfo);
	User getUserByUserId(String userId);
	
	int updateUserInformation(String department, String position, String name, String userId);
	int deleteUserInformation(String userId);
}

// User Service Implementation 클래스
@Service("userService")
public class UserServiceImpl implements UserService {
	@Autowired
	UserRepository userRepository;
	
	@Autowired
	UserRepositorySupport userRepositorySupport;
	
	@Autowired
	PasswordEncoder passwordEncoder;
	
	@Override
	public User createUser(UserRegisterPostReq userRegisterInfo) {
		User user = User.builder()
				.userId(userRegisterInfo.getUserId())
				.password(passwordEncoder.encode(userRegisterInfo.getPassword()))
				.position(userRegisterInfo.getPosition())
				.department(userRegisterInfo.getDepartment())
				.name(userRegisterInfo.getName())
				.build();
		return userRepository.save(user);
	}

	@Override
	public User getUserByUserId(String userId) {
		User user = userRepositorySupport.findUserByUserId(userId).orElse(null);
		return user;
	}

	@Override
	public int updateUserInformation(String department, String position, String name, String userId) {
		return userRepository.updateUserInfo(department, position, name, userId);
	}

	@Override
	public int deleteUserInformation(String userId) {
		return userRepository.deleteUserInfo(userId);
	}
}
```

- `UserService` 인터페이스에는 메서드에 대한 정의를 하고, `UserServiceImpl` 클래스에서 이를 확장하여 메서드를 실제적으로 구현한다.
- `@Service`
  - 해당 클래스가 Service라는 것을 스프링에게 알리기 위한 어노테이션
- `@Override`
  - 인터페이스에 정의된 메서드를 오버라이드하여 메서드 본체를 작성할 수 있다.
- 아래 참고의 여러 블로그 글에도 언급되어 있듯이, Service 인터페이스와 이를 확장한 ServiceImpl 구현 클래스가 1:1의 구조일 때도 단지 다른 개발자들이 두 개를 관습적으로 분리하기 때문에 나눠 놓는다는 내용이 많이 쓰여 있다. 왜 그럴까? 에 대한 고민과 여러가지 해답에 대한 이해가 필요하다.

- 참고
  - https://wildeveloperetrain.tistory.com/49 → 가장 이해가 잘 되는 글
  - https://velog.io/@aquarius1997/Service%EC%99%80-ServiceImpl
  - https://elvis-note.tistory.com/entry/9-Spring-MVC-2-Service%EC%99%80-ServiceImpl
  - https://multifrontgarden.tistory.com/97
  - https://cheese10yun.github.io/spring-oop-04/
  - https://m.blog.naver.com/scw0531/220988401816

<br>

#### Controller

<br>

#### Swagger



### 인증

`[POST] /auth/login`

- ID, 비밀번호를 입력해서 인증 및 JWT 토큰을 발급받는 API

```java
// controller - AuthController

@Api(value = "인증 API", tags = {"Auth."})
@RestController
@RequestMapping("/api/v1/auth")
public class AuthController {
	@Autowired
	UserService userService;
	
	@Autowired
	PasswordEncoder passwordEncoder;
	
	@PostMapping("/login")
	@ApiOperation(value = "로그인", notes = "<strong>아이디와 패스워드</strong>를 통해 로그인 한다.") 
    @ApiResponses({
        @ApiResponse(code = 200, message = "성공", response = UserLoginPostRes.class),
        @ApiResponse(code = 401, message = "인증 실패", response = BaseResponseBody.class),
        @ApiResponse(code = 404, message = "사용자 없음", response = BaseResponseBody.class),
        @ApiResponse(code = 500, message = "서버 오류", response = BaseResponseBody.class)
    })
	public ResponseEntity<UserLoginPostRes> login(@RequestBody @ApiParam(value="로그인 정보", required = true) UserLoginPostReq loginInfo) {
		String userId = loginInfo.getId();
		String password = loginInfo.getPassword();
		
		User user = userService.getUserByUserId(userId);
        // 로그인 시도하려는 회원이 존재하지 않을 경우, 404 에러메시지로 응답
        if(user==null) {
            return ResponseEntity.ok(UserLoginPostRes.of(404, "No Such User", null));
        }
		// 로그인 요청한 유저로부터 입력된 패스워드 와 디비에 저장된 유저의 암호화된 패스워드가 같은지 확인.(유효한 패스워드인지 여부 확인)
		if(passwordEncoder.matches(password, user.getPassword())) {
			// 유효한 패스워드가 맞는 경우, 로그인 성공으로 응답.(액세스 토큰을 포함하여 응답값 전달)
			return ResponseEntity.ok(UserLoginPostRes.of(200, "Success", JwtTokenUtil.getToken(userId)));
		}
		// 유효하지 않는 패스워드인 경우, 로그인 실패로 응답.
		return ResponseEntity.status(401).body(UserLoginPostRes.of(401, "Invalid Password", null));
	}
}
```

- 에러 처리 (404)

- https://jdm.kr/blog/234

- https://www.daleseo.com/java8-optional-after/#optional-%EA%B0%9D%EC%B2%B4-%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0

  .get()

  .orElse()



##### properties > yml convert

- properties 대신 yml 파일로 관리하기 위해 변환
- http://mageddo.com/tools/yaml-converter

```properties
#it will be set build date by gradle. if this value is @build.date@, front-end is development mode
build.date=@build.date@
server.port=8080
server.address=localhost
server.servlet.contextPath=/
# Charset of HTTP requests and responses. Added to the "Content-Type" header if not set explicitly.
server.servlet.encoding.charset=UTF-8
# Enable http encoding support.
server.servlet.encoding.enabled=true
# Force the encoding to the configured charset on HTTP requests and responses.
server.servlet.encoding.force=true

# for SPA
spring.resources.static-locations=classpath:/dist/
spa.default-file=/dist/index.html
spring.mvc.throw-exception-if-no-handler-found=true
spring.resources.add-mappings=false

# Swagger
springfox.documentation.swagger.use-model-v3=false

# database
spring.jpa.hibernate.naming.implicit-strategy=org.springframework.boot.orm.jpa.hibernate.SpringImplicitNamingStrategy
spring.jpa.hibernate.naming.physical-strategy=org.springframework.boot.orm.jpa.hibernate.SpringPhysicalNamingStrategy
spring.jpa.hibernate.ddl-auto=update
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL57Dialect
spring.data.web.pageable.one-indexed-parameters=true
spring.datasource.url=jdbc:mysql://localhost:3306/ssafy_web_db?useUnicode=true&characterEncoding=utf8&serverTimezone=Asia/Seoul&zeroDateTimeBehavior=convertToNull&rewriteBatchedStatements=true
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.hikari.username=root
spring.datasource.hikari.password=root1234!

# sql 보기
spring.jpa.show_sql=true

# jwt
jwt.secret=dyAeHubOOc8KaOfYB6XEQoEj1QzRlVgtjNL8PYs1A1tymZvvqkcEU7L1imkKHeDa
# unit is ms. 15 * 24 * 60 * 60 * 1000 = 15days
jwt.expiration=1296000000

#logging
logging.file.name=./ssafy-web.log
logging.level.root=INFO
logging.level.com.samsung.security=DEBUG
logging.level.org.springframework.web=DEBUG
logging.level.org.apache.tiles=INFO
logging.level.org.sringframework.boot=DEBUG
logging.level.org.sringframework.security=DEBUG

spring.devtools.livereload.enabled=true

#gzip compression
server.compression.enabled=true
server.compression.mime-types=application/json,application/xml,text/html,text/xml,text/plain,application/javascript,text/css

#for health check
management.servlet.context-path=/manage
management.health.db.enabled=true
management.health.default.enabled=true
management.health.diskspace.enabled=true
```

```yaml
management:
  health:
    diskspace:
      enabled: 'true'
    default:
      enabled: 'true'
    db:
      enabled: 'true'
  servlet:
    context-path: /manage
spa:
  default-file: /dist/index.html
logging:
  level:
    org:
      sringframework:
        boot: DEBUG
        security: DEBUG
      apache:
        tiles: INFO
      springframework:
        web: DEBUG
    root: INFO
    com:
      samsung:
        security: DEBUG
  file:
    name: ./ssafy-web.log
server:
  servlet:
    encoding:
      enabled: 'true'
      force: 'true'
      charset: UTF-8
    contextPath: /
  address: localhost
  port: '8080'
  compression:
    enabled: 'true'
    mime-types: application/json,application/xml,text/html,text/xml,text/plain,application/javascript,text/css
spring:
  jpa:
    hibernate:
      naming:
        implicit-strategy: org.springframework.boot.orm.jpa.hibernate.SpringImplicitNamingStrategy
        physical-strategy: org.springframework.boot.orm.jpa.hibernate.SpringPhysicalNamingStrategy
      ddl-auto: update
    properties:
      hibernate:
        dialect: org.hibernate.dialect.MySQL57Dialect
    show_sql: 'true'
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    hikari:
      password: *********
      username: root
    url: jdbc:mysql://localhost:3306/ssafy_web_db?useUnicode=true&characterEncoding=utf8&serverTimezone=Asia/Seoul&zeroDateTimeBehavior=convertToNull&rewriteBatchedStatements=true
  data:
    web:
      pageable:
        one-indexed-parameters: 'true'
  mvc:
    throw-exception-if-no-handler-found: 'true'
  devtools:
    livereload:
      enabled: 'true'
  resources:
    static-locations: classpath:/dist/
    add-mappings: 'false'
build:
  date: '@build.date@'
jwt:
  expiration: '1296000000'
  secret: dyAeHubOOc8KaOfYB6XEQoEj1QzRlVgtjNL8PYs1A1tymZvvqkcEU7L1imkKHeDa
springfox:
  documentation:
    swagger:
      use-model-v3: 'false'
```

