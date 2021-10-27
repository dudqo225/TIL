Django | REST API

### 목차

>- HTTP
>- RESTful API
>- Response
>- Single Model
>- 1:N Relation

<br>

### HTTP

- HyperText Transfer Protocol
- 웹상에서 컨텐츠를 전송하기 위한 약속
- 웹에서 이루어지는 데이터 교환의 기초
  - 요청(request)
    - 클라이언트에 의해 전송되는 메시지
  - 응답(response)
    - 서버에서 응답으로 전송되는 메시지
- 기본 특성
  - Stateless
  - Connectless
- 쿠키와 세션을 통해 서버 상태를 요청과 연결
- HTTP request Methods
  - GET, POST, PUT, DELETE...
- HTTP response status codes
  - 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄
  - 5개의 그룹
    - Informational responses (1xx)
    - Successful responses (2xx)
    - Redirection messages (3xx)
    - Client error responses (4xx)
    - Server error responses (5xx)

#### URI (URL, URN)

- URI (Uniform Resource Identifier)
  - 통합 자원 식별자
  - 인터넷 자원을 식별하는 유일한 주소 (정보의 자원을 표현)
  - 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열
  - 하위 개념
    - URL, URN

- URL (Uniform Resource Locator)
  - 통합 자원 위치
  - 네트워크 상에 자원이 어디 있는지 알려주기 위한 약속
  - 과거에는 실제 자원의 위치를 나타냈으나 현재는 추상화된 의미론적 구성
  - 웹 주소 or 링크라고 불림
- URN (Uniform Resource Name)
  - 통합 자원 이름
  - URL과 달리 자원의 위치에 영향을 받지않는 유일한 이름 역할
  - ex.
    - ISBN

- URI의 구조
  - Scheme (protocol)
    - 브라우저가 사용해야 하는 프로토콜
    - http(s), data, file, ftp, malito
  - Host (Domain name)
    - 요청을 받는 웹 서버의 이름
    - IP Adress를 직접 사용할 수 있지만, 불편함
  - Port
    - 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 문 (gate)
    - HTTP 프로토콜의 표준 포트
      - HTTP 80
      - HTTPS 443
  - Path
    - 웹 서버 상의 리소스 경로
    - 물리적 위치가 아닌 추상화 형태의 구조로 표현
  - query (Identifier)
    - Query String Parameters
    - 웹 서버에 제공되는 추가적인 매개변수
    - `&` 로 구분되는 key-value 목록
  - Fragment
    - `Anchor`
    - 자원 안에서의 북마크의 한 종류를 나타냄
    - 브라우저에게 해당 문서의 특정 부분을 보여주기 위한 방법
    - fragment identifier(부분 식별자)라고 부르며 # 뒤의 부분은 요청이 서버에 보내지지 않음

<br>

### RESTful API

#### API

- Application Programming Interface

- 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스

  - 애플리케이션과 프로그래밍으로 소통하는 방법
  - CLI - 명령줄, GUI - 그래픽(아이콘), API - 프로그래밍을 통해 특정한 기능을 수행

- Web API

  - 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세
  - 현재 웹 개발은 모든 것을 직접 개발하기보다 여러 Open API를 활용하는 추세

- 응답 데이터 타입

  - HTML, XML, JSON

  
