# Django | Model

### 목차

> - Model
>
> - ORM
>
> - Migrations
>
> - Database API
>
> - CRUD
>
> - Admin Site

<br>

### 1. Model

#### Model 이란?

- 단일한 데이터에 대한 정보를 가짐
  - 사용자가 저장하는 데이터의 필수적인 `필드` 와 `동작` 을 포함
- 저장된 데이터베이스의 구조(layout)
- `django` 는 `model` 을 통해서 데이터에 접속하고 관리
- 일반적으로 각 `model` 은 하나의 DB 테이블에 매핑(Mapping)
- 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구

<br>

#### Database

- 데이터베이스(DB)
  - 체계화된 데이터의 모임
- 쿼리(Query)
  - 데이터를 조회하기 위한 명령어
  - 조건에 맞는 데이터를 추출, 조작하는 명령어
- 기본 구조
  - 스키마(Schema)
    - 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조
  - 테이블(Table)
    - 열(column), 필드(field), 속성
    - 행(row), 레코드(record), 튜플
  - PK(기본키)
    - 각 레코드의 고유값으로 **Primary Key**
    - 반드시 설정해야 하며, DB 관리 및 관계 설정시 주요하게 활용됨

<br>

### 2. ORM

#### ORM 이란?

- Object-Relational-Mapping
- 객체 지향 프로그래밍(OOP) 언어를 사용하여 호환되지 않는 유형의 시스템 간 데이터를 변환하는 프로그래밍 기술
  - ex. Django ↔ SQL
- OOP 프로그래밍에서 RDBMS를 연동할 때, 호환되지 않는 데이터를 변환하는 프로그래밍 기법이다.
- Django는 내장 Django ORM을 사용

<br>

#### 장점과 단점

- 장점
  - SQL을 잘 알지 못하더라도 DB 조작이 가능하다
  - SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인해 높은 **생산성**을 보인다
    - 현대 웹 프레임워크의 핵심은 웹 개발 속도를 높이는 것 (생산성)
- 단점
  - ORM 만으로는 완전한 서비스를 구현하기 어려운 경우가 있다

<br>

### 3. Migrations

#### Migrations

- `django` 가 `model` 에 생긴 변화를 DB에 반영하는 방법
- 마이그레이션 실행 및 DB 스키마를 다루기 위한 명령어
  - `makemigrations`
    - `model` 을 변경한 것에 기반한 새로운 마이그레이션(설계도)을 만들 때 사용
  - `migrate`
    - 마이그레이션을 DB에 반영하기 위해 사용
    - 설계도를 실제 DB에 반영하는 과정
    - 모델에서의 변경사항들과 DB의 스키마가 동기화를 이룸
  - `sqlmigrate`
    - 마이그레이션에 대한 SQL 구문을 보기 위해서 사용
    - 마이그레이션이 SQL 문으로 어떻게 해석되고 동작할지 미리 확인 가능
  - `showmigrations`
    - 프로젝트 전체의 마이그레이션 상태를 확인
    - 마이그레이션 파일들이 `migrate` 되었는지 안되었는지 여부를 확인

#### Migration 3단계

1. `models.py`
   - model 변경사항 발생
2. `$ python manage.py makemigrations`
   - migrations 파일 생성
3. `$ python manage.py migrate`
   - DB 적용

<br>

##### DateTimeField's options

- `auto_now_add`
  - 최초 생성 일자
  - django ORM이 최초 `insert` 시에만 현재 날짜와 시간으로 갱신
- `auto_now`
  - 최종 수정 일자
  - django ORM이 `save` 를 할 때마다 현재 날짜와 시간으로 갱신

<br>

### 4. Database API

- DB를 조작하기 위한 도구
- django가 기본적으로 ORM을 제공함에 따른 것으로, DB를 편하게 조작할 수 있도록 도움
- Model을 만들면 django는 객체를 만들고, 읽고, 수정하고, 지울 수 있는(CRUD) database-abstract API를 자동으로 만든다
- `database-abstract API` 혹은 `database-access API` 라고도 함

<br>

#### DB API

- DB API 구문 예시
  - `Article.objects.all()`
    - `Article` : Class Name
    - `objects` : Manager
    - `all()` : QuerySet API

- Manager
  - django 모델에 데이터베이스 query 작업이 제공되는 인터페이스
  - 기본적으로 모든 django 모델 클래스에 **`objects` 라는 Manager를 추가**
- QuerySet
  - 데이터베이스로부터 전달받은 객체 목록
  - queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
  - DB로부터 조회, 필터, 정렬 등을 수행할 수 있다

#### Django shell

- 일반 파이썬 쉘을 통해서는 장고 프로젝트 환경에 접근할 수 X
- 장고 프로젝트 설정이 로드된 파이썬 쉘(+shell_plus)을 활용해서 DB API 구문을 테스트
- 기본 Django shell 보다 많은 기능을 제공하는 `shell_plus` 설치

```python
# 라이브러리 설치
pip install ipython
pip install django-extensions

# settings.py 에 앱 등록(django_extensions) 후 shell_plus 실행
python manage.py shell_plus
```

<br>

### 5. CRUD

- 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능

  - `Create` (생성), `Read` (읽기), `Update` (갱신), `Delete` (삭제)를 묶어서 일컫는 말

  - Create 생성

    - `save()` method

      - Saving objects
      - 객체를 DB에 저장
      - 데이터 생성시 save()를 호출하기 전에는 객체가 저장되지 않고, ID 값이 무엇인지도 알 수 없음

    - `save()` 없이 바로 생성하는 방법

      - `.create()` 사용
      - ex. `Article.objects.create(title='제목', content='내용')` 

    - str method

      - 표준 파이썬 클래스의 메소드인 str()을 정의해서 각 object가 사람이 읽을 수 있는 문자열을 반환하도록 할 수 있다
      - 작성 후에는 반드시 shell_plus를 재시작해야 함

      ```python
      def __str__(self):
          return self.title
      ```

  - Read 조회

    - QuerySet API method를 사용한 다양한 조회를 하는 것이 중요하다
    - 분류
      - Return new querysets
      - Do not return querysets
    - `all()`
      - queryset을 리턴. 리스트는 아니지만 리스트와 거의 비슷하게 동작함
    - `get()`
      - 주어진 lookup 매개변수와 일치하는 객체를 반환
      - 객체를 찾을 수 없으면 `DoesNotExist` 예외를 발생시키고, 둘 이상의 객체를 찾으면 `MultipleObjectReturned` 예외를 발생시킨다.
      - `PK` 와 같이 고유성(Unique)을 보장하는 조회에서 사용해야 한다.
    - `filter()`
      - 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
      - 객체를 찾을 수 없으면 비어 있는 QuerySet을 반환

  - Update 갱신

    - 바꾸고자 하는 객체를 먼저 Read한 후, 인스턴스 변수 값을 변경

    ```python
    article = Article.objects.get(pk=1) # pk가 1인 객체를 article에 저장
    article.title = 'byebye' # title 값을 바꾼다
    article.save() # 변경 후 반드시 저장
    ```

  - Delete 삭제

    - `delete()`
    - QuerySet의 모든 행에 대해 SQL 삭제 쿼리를 수행하고, 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 `Dict`를 반환

<br>

#### HTTP Method

- **GET**
  - 특정 리소스를 가져오도록 요청할 때 사용
  - **반드시!!** 데이터를 가져올 때만 사용
  - DB에 변화를 주지 않음
  - CRUD에서 **`R`** 역할을 담당한다
- **POST**
  - 서버로 데이터를 전송할 때 사용
  - 리소스를 생성 or 변경하기 위해 데이터를 **HTTP body에 담아서 전송** (URL에 노출되지 않음)
  - 서버에 변경사항을 만듦
  - CRUD에서 **`C/U/D`** 역할을 담당한다

<br>

#### 사이트 간 요청 위조 (Cross-Site-Request-Forgery)

- 웹 애플리케이션 취약점 중 하나로, 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 해서 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
- django는 `CSRF`에 대항하여 middleware 와 template tag 를 제공

- CSRF 공격 방어
  - Security Toekn 사용 방식 (CSRF Token)
    - 사용자 데이터에 임의의 난수 값을 부여해서 매 요청마다 해당 난수 값을 포함시켜 전송시키도록 함
    - 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증
  - 데이터 변경이 가능한 `POST`, `PATCH`, `DELETE` Method 등에 적용 (`GET`은 제외)
  - django는 csrf token 템플릿 태그를 제공
    - `{% csrf_token %}`
    - `input type`이 `hidden`으로 작성되고 `value`는 django에서 생성한 `hash` 값이 들어있음
    - 해당 태그가 없으면 django 서버는 403 forbidden을 응답

<br>

##### redirect()

- 새 url로 되돌림
- 인자에 따라서 HttpResponseRedirect를 반환
- 브라우저는 현재 경로에 따라 전체 URL을 재구성(reconstruct)
- 사용 가능한 인자
  - model
  - view name
  - absolute / relative URL

<br>

### 6. Admin Site

#### Automatic admin interface

- 서버 관리자가 활용하기 위한 페이지
- Model class를 `admin.py` 에 등록하고 관리
- `django.contrib.auth` 모듈에서 제공된다
- 레코드 생성여부 확인할 때 사용가능하고, 직접 레코드를 삽입할 수도 있다

##### admin 생성

```bash
$ python manage.py createsuperuser
```

- 관리자 계정 생성 후 `/admin` 페이지에 가서 관리자 로그인
- `auth`에 관련된 기본 테이블이 생성되지 않으면 관리자 계정을 생성할 수 X

##### admin 등록

```python
from .models import <ClassName>
admin.site.register(<ClassName>)
```

- `admin.py`는 관리자 사이트에 객체가 관리자 인터페이스를 가지고 있다는 것을 알려준다
- `models.py` 에 정의한 `__str__` 의 형태로 객체가 표현됨

##### ModelAdmin options

- list_display

  - models.py에서 정의한 각 속성들의 값을 admin 페이지에 출력하도록 설정

  ```python
  class ArticleAdmin(admin.ModelAdmin):
      list_display = ('pk', 'id', 'title', 'content')
  
  admin.site.register(Article, ArticleAdmin)
  ```

- list_filter, list_display_links 등 다양한 optins은 공식문서 참고

  - [django 공식문서](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#modeladmin-options)



