# Web | JWT

### Authentication

- 인증, 입증
- 사용자가 누구인지 확인하는 행위 (verifying who a user is)
- Credentials(비밀번호, 얼굴인식) 검증
- 모든 보안 프로세스의 첫번째 단계 (기본!!)
- *401 Unauthorized*
  - HTTP 표준에서는 미승인(Unauthorized)로 표현되지만, 의미상 이 응답은 비인증(Unauthenticated)를 의미

### Authorization

- 권한 부여, 허가
- 사용자에게 특정 리소스 or 기능에 대한 엑세스 권한을 부여하는 과정(절차) (verifying what they have access to)
- 보안 환경에서 권한 부여는 항상 인증(Authentication)을 따라야 함
  - ex. 사용자가 조직에 대한 엑세스 권한을 부여받기 전에 자신의 ID가 진짜인지를 먼저 확인해야 함
- 서류 등급, 웹페이지에서 글을 조회/삭제/수정할 수 있는 권한, 제한 구역
  - 인증(Authentication)되었어도 모든 권한을 부여받는 것은 아님
- *403 Forbidden*
  - 401과 다른점은 서버는 클라이언트가 누구인지 알고 있음

<br>

## JWT

- **J**SON **W**eb **T**oken
- JSON 포맷을 활용하여 요소간 안전하게 정보를 교환하기 위한 표준 포맷
- 암호화 알고리즘에 의한 디지털 서명이 되어 있기 때문에 JWT 자체로 검증 가능하고 신뢰할 수 있는 정보 교환 체계
- **JWT 자체가 필요한 정보를 모두 갖고 있기 때문에 (Self-Contained)** 이를 검증하기 위한 다른 검증 수단이 필요 없음

- 특징
  - 기본 토큰 인증 체계와 달리 JWT 인증 확인은 DB를 사용하여 토근의 유효성을 검사할 필요가 없음
  - JWT 자체가 인증에 필요한 정보를 갖고 있기 때문 (self-contained)
  - vs. 세션 기반 or 기본 토큰 기반 인증과의 핵심 차이점
- 활용 이유
  - Session 기반 방식에 비해 HTML, HTTP 환경에서 사용하기 용이
    - 유저의 session 정보를 Server에 보관해야 함
    - JWT는 Client Side에 토큰 정보를 저장하고 필요한 요청에 유효한 토큰을 같이 넣어 보내면 그 자체가 인증 수단
  - 보안 수준
    - 특정 요소 하나만 변경되어도 모든 데이터가 바뀌기 때문에 위/변조가 불가능
  - JSON의 범용성
  - Server 메모리에 정보를 저장하지 않아 Server의 자원 절약 가능

- 구조
  - Header
    - 토큰 유형(Type)과 Hashing Algorithm으로 구성
  - Payload
    - 토큰에 넣을 정보
    - claim은 정보의 한 조각. payload에 여러 개의 claim을 넣을 수 있음
  - Signature
    - Header와 Payload의 Encoding 값을 더하고, Private Key로 Hashing하여 생성

#### JWT 로그아웃

- 기본적으로 Logout 요청을 보내서 브라우저에서 토큰 정보를 삭제 처리
- 로그아웃 하더라도 유효한 토큰이 어딘가에 남아있다면 누군가 '인증'을 할 수 있음
- 위와 같은 문제에 대한 최소한의 안전 장치 설정
  - 토큰의 만료 시간 설정
  - 브라우저 LocalStorage에 저장된 토큰 삭제
  - 블랙 리스트 설정
    - 더 이상 유효하지 않거나 만료되지 않은 모든 토큰을 블랙리스트 처리

<br>

#### set_password()

- 비밀번호 해싱을 처리하여 사용자의 암호를 문자열 데이터로 설정
- User 객체를 저장하지는 않음

<br>

#### REST framework JWT Auth Package

- DRF에 대한 JWT Authentication 지원 패키지

```bash
$ pip install djangorestframework-jwt
```

<br>

- DRF 각 view 함수에 대한 default 권한 및 인증 설정
- 회원 인증 여부와 JWT 토큰 인증에 관한 설정

```python
# settings.py 전역 설정

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
    	'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
    	'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}
```

<br>

- url.py에 URL 경로를 추가하여, 사용자 이름/비밀번호가 포함된 POST 요청을 통해 토큰을 얻을 수 있도록 함

```python
# accounts/urls.py

from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    ...,
    path('api-token-auth/', obtain_jwt_token),
]
```

<br>

#### Login

- 브라우저 localStorage에 JWT 저장

```js
// Login.vue

methods: {
    login: function () {
        ...
        .then(res => {
            localStorage.setItem('jwt', res.data.token)
            this.$emit('login')
            this.$router.push({ name: 'TodoList' })
        })
    }
}
```

<br>

#### Logout

- 메서드 작성

```js
// App.vue

methods: {
    logout: function () {
        this.isLogin = false
        localStorage.removeItem('jwt')
        this.$router.push({ name: 'Login' })
    }
}
```

<br>

#### Signup 문제 해결

- IsAuthenticated로 인해 인증되지 않은 사용자에 대한 권한을 거부하고 있음
- 회원가입에서는 불필요한 인증과정이기 때문에 별도 데코레이터를 작성해서 override 해야 함

- DRF Settings

```python
# accounts/views.py

from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    ...
```

<br>

#### CRUD with Authentication

- JWT 인증 문제
  - 401 에러 발생
  - 토큰이 없는 요청은 IsAuthenticated의 유효성 검사를 통과하지 못하기 때문
  - 인증이 필요한 요청에 브라우저에 저장된 JWT를 함께 보내야 함
  - HTTP request header에 `Authorization: JWT <my_token>` 형식으로 보내야 함

- JWT 설정 및 적용

```js
// TodoList.vue

methods: {
    setToken: function () {
        const token = localStorage.getItem('jwt')
        const config = {
            Authorization: `JWT ${token}`
        }
        return config
    }
}
```

- 각각의 메서드에 `headers: this.setToken()` 을 호출하여 JWT를 함께 보낼 수 있도록 수정

```js
axios({
    ...
    headers: this.setToken(),
})
```

