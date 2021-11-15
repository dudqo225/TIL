# JavaScript | SOP & CORS

### SOP

- **S**ame-**O**rigin **P**olicy
- 동일 출처 정책
- 특정 출처(origin)에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한하는 보안 방식
- 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임

#### Origin (출처)

- URL 간 **Protocol, Port, Host**가 모두 같아야 동일한 출처라고 본다.

![image-20211115174353547](javascript_sop_cors.assets/image-20211115174353547.png)

- 그림과 같이, Path를 제외한 나머지 3가지가 동일해야 같은 Origin !!!

<br>

### CORS

- **C**ross-**O**rigin **R**esource **S**haring
- 교차 출처 리소스(자원) 공유
- 추가 HTTP headers를 사용하여, 특정 출처에서 실행중인 웹 애플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제
- 리소스가 자신의 출처(Protocol, Host(Domain), Port) 와 다를 때 교차 출처 HTTP 요청을 실행
- 보안 상의 이유로 브라우저는 기본적으로 교차 출처 HTTP 요청을 제한
  - 예를 들어 `XMLHttpRequest`는 SOP를 따름
- 출처가 다른 리소스를 불러오려면 올바른 CORS header를 포함한 응답을 반환해야 함
- CORS Policy ↔ SOP

#### CORS 장점

- 브라우저 & 웹 애플리케이션 보호
  - 악의적인 사이트의 데이터를 가져오지 않도록 사전에 차단 가능
  - 응답으로 받는 자원에 대한 최소한의 검증 가능
  - 서버는 정상적으로 응답하더라도 브라우저에서 차단
- Server의 자원 관리
  - 누가 해당 리소스에 접근할 수 있는지 관리 가능

#### Access-Control-Allow-Origin 응답 헤더

- 이 응답이 주어진 출처/리소스/Origin 으로 부터 요청 코드와 공유될 수 있는지를 나타냄
- Ex.
  - `Access-Control-Allow-Origin: *`
  - 브라우저 리소스에 접근하는 임의의 출처/리소스/Origin 에 대해 요청을 허용한다고 알리는 응답에 포함
  - `*` 은 모든 도메인에서 접근할 수 있음을 의미
  - 특정 Origin 하나를 명시할 수도 있음

##### django-cors-headers 라이브러리

- 응답에 CORS deader를 추가해주는 라이브러리
- 다른 출처에서 보내는 django 애플리케이션에 대한 브라우저 내의 요청을 허용
- django APP이 header 정보에 CORS를 설정한 상태로 응답할 수 있도록 도와주며, 이 설정을 통해서 브라우저는 다른 리소스/출처/Origin에서 요청을 보내는 것이 가능해짐

```bash
# 설치

$ pip install django-cors-headers
```



```django
# settings.py

INSALLED_APPS = [
	...
	'corsheaders',
]

MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
	...
]

CORS_ALLOW_ALL_ORIGINS = True
```

