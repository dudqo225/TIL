# Django | Static Files

### 목차

> - Static files
> - Media files
> - Image Upload
> - Image Resizing

<br>

### 1. Static files

#### Intro

- 정적 파일
- 응답할 때 별도의 처리 없이 파일 내용을 보여주면 되는 파일
- ex. 웹사이트는 일반적으로 이미지, JS, CSS 같은 미리 준비된 움직이지 않는 파일을 제공한다.
- Django에서는 이러한 파일들을 "static file" 이라고 함

#### static file 구성

- `django.contrib.staticfiles`가 INSTALLED_APPS에 포함되어 있는지 확인
- `settings.py` 에서 STATIC_URL 정의
- template에서 `{% load static %}` 태그를 사용해서 지정된 상대경로에 대한 URL 빌드
- APP의 static 폴더에 파일을 저장
  - ex. `app_name/static/app_name/example.jpg`
- Django template tag
  - `load`
    - 사용자 정의 템플릿 태그 세트를 로드
    - 로드하는 라이브러리, 패키지에 등록된 모든 태그 & 필터 로드
  - `static`
    - STATIC_ROOT에 저장된 정적 파일에 연결

#### The Staticfiles App

- `STATIC_ROOT`
  - collectstatic이 배포를 위해서 정적 파일을 수집하는 폴더의 절대 경로
  - 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로임
  - `settings.py`의 DEBUG 값이 True로 설정되어 있으면 해당 값은 적용되지 않는다.
    - 개발자가 직접 작성하지 않으면 settings.py에 작성되어 있지 않음
  - 실제 서비스환경(배포 환경)에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함
- `STATIC_URL`
  - STATIC_ROOT에 있는 정적 파일을 참조할 때 사용하는 URL
  - 개발 단계에서는 정적파일이 저장되어 있는 `app/staic/경로` 및 `STATICFILES_DIRS` 에 정의된 추가 경로들을 탐색
  - 실제 파일 or 디렉토리가 아니고, URL로만 존재
  - 비어 있지 않은 값으로 설정할 경우 반드시 `/` 로 끝나야 함
- `STATICFILES_DIRS`
  - `app/static/` 디렉토리 경로를 사용하는 기본 경로 이외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
  - 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함

<br>

### 2. Media file

#### Intro

- 미디어 파일
- 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)
- 유저가 업로드한 모든 정적 파일

#### Model field

- `ImageField`
  - 이미지 업로드에 사용하는 모델 필드
  - FileField를 상속받는 서브 클래스이므로 FileField의 모든 속성/메서드 사용이 가능하고, 사용자에 의해 업로드된 객체가 유효한 이미지인지 검사함
  - ImageField 인스턴스는 최대 길이 100자인 문자열로 DB에 생성, `max_length` 인자를 사용하여 최대 길이를 변경할 수 있음
  - 사용하려면 `Pillow` 라이브러리가 필수

- `FileField`

  - 파일 업로드에 사용하는 모델 필드

  - 2개의 선택인자를 가지고 있음

    - `upload_to`

      - 업로드 디렉토리와 파일 이름을 설정하는 2가지 방법 제공

        - 문자열 값 or 경로 지정

        ```python
        # models.py
        
        class MyModel(models.Model):
            upload = models.FileField(upload_to='uploads/')
            # or
            upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
        ```

        - 함수 호출
          - 2개의 인자(instance, filename)을 사용
            - instance
              - FileField가 정의된 모델의 인스턴스
              - 대부분 객체가 아직 DB에 저장되지 않았으므로 PK 값이 아직 없을 수 있음
            - filename
              - 기존 파일에 제공된 파일의 이름

        ```python
        # models.py
        
        def articles_image_path(instance, filename):
            return f'user_{instance.user.pk}/{filename}'
        
        class Article(models.Model):
            image = models.ImageField(upload_to=articles_image_path)
        ```

    - ~~`storage`~~

#### ImageField 와 FileField 를 사용하기 위한 단계

- `settings.py` 에 MEDIA_ROOT, MEDIA_URL 설정
- `upload_to` 속성을 정의해서 업로드된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정
- 업로드 된 파일 경로는 django가 제공하는 `url` 속성을 통해 얻을 수 있음

```python
<img src="{{ article.image.url }}" alt="{{ article.image }}">
```

- MEDIA_ROOT

  - 사용자가 업로드한 파일을 보관할 디렉토리의 절대 경로
  - django는 성능을 위해 업로드 파일을 DB에 저장하지 않음
    - DB에 저장되는 것은 **파일의 경로**
  - **MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야 함**

  ```python
  # settings.py
  
  MEDIA_ROOT = BASE_DIR / 'media'
  ```

- MEDIA_URL
  - MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
  - 업로드된 파일의 주소(URL)을 만들어 주는 역할
  - 비어 있지 않은 값으로 설정한다면 반드시 `/` 로 끝나야 함
  - **MEDIA_URL은 STATIC_URL과 반드시 다른 경로로 지정해야 함**

```python
# PJT/urls.py

...
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 업로드 된 파일의 URL : settings.MEDIA_URL
# 위 URL을 통해서 참조하는 파일의 실제 위치 : settings.MEDIA_ROOT
```

- STATIC_URL & MEDIA_URL
  - 모두 서버에 요청해서 조회하는 것
  - 서버에 요청하기 위한 url을 `urls.py`가 아닌 `settings`에 먼저 작성/정의한 후 `urlpatterns`에 추가하는 형식

<br>

### 3. Image Upload

#### CREATE

- ImageField 작성

  - `upload_to='images/'`
    - 실제 이미지가 저장되는 경로를 지정
  - `blank=True`
    - 이미지 필드에 빈 값(문자열)이 허용되도록 설정
      - DB에 `''`(빈 문자열)이 저장됨
    - 이미지를 선택적으로 업로드할 수 있도록 하기 위함
    - 기본값은 False 임
    - 유효성 검사(`is_valid`)에 사용 됨
      - blanck가 True일 경우에는 form 유효성 검사에서 빈 값을 입력할 수 있음

  - `null`
    - 기본 값은 False
    - True면 django는 빈 값을 DB에 `NULL` 로 저장
    - 주의 사항
      - `CharField`, `TextField` 같은 문자열 기반 필드에는 사용하는 것을 지양
      - 문자열 기반 필드에 True로 설정 시, `데이터 없음(no data)` 에 `빈 문자열` 과 `NULL` 2가지 가능한 값이 있음을 의미하게 됨
      - django는 NULL이 아닌 빈 문자열을 사용하는 것이 규칙임
  - `blank` vs `null`
    - blank : Validation-related
    - null : Database-related
    - 문자열 / 비문자열 기반 필드 모두 null 옵션은 DB에만 영향을 미치므로, form에서 빈 값을 허용하려면 `blank=True`를 설정

- `form` 태그 내부에 `enctype` 인코딩 속성 설정
  - `multipart/form-data`
    - 파일/이미지 업로드 시에 반드시 사용해야 함
    - 전송되는 데이터의 형식을 지정
    - `<input type="file">`을 사용할 경우에 사용
  - ~~`application/x-www-form-urlencoded`~~
  - ~~`text/plain`~~
- `input` 태그에 `accept` 속성 지정
  - accept
    - 입력 허용할 파일 유형을 나타내는 문자열
    - **고유 파일 유형 지정자** (unique file type specifiers)를 쉼표로 구분
    - 파일 검증을 하는 것은 아님
      - 이미지만 accept으로 설정해두어도 비디오나 오디오 파일을 제출할 수 있음

- `views.py` 수정
  - 업로드한 파일은 `request.FILES` 객체로 전달됨

<br>

### READ

#### 이미지 경로 불러오기

- `article.image.url` == 업로드 파일의 경로
- `article.image` == 업로드 파일의 파일 이름

<br>

### UPDATE

#### 이미지 수정하기

- 이미지는 바이너리 데이터(하나의 덩어리)이기 때문에 텍스트처럼 **일부만 수정하는 것은 불가능**
- 새로운 파일을 덮어 씌우는 방식을 사용

- `{% if %}{% endif %}` 블록으로 image가 없는 게시글의 경우 detail 페이지를 출력하지 못하는 문제를 해결

<br>

### 4. Image Resizing

#### 이미지 크기 변경하기

- 실제 원본 이미지를 서버에 그대로 업로드하는 것은 서버에 부담이 매우 큰 작업
- `<img>` 태그에서 width/height 로 사이즈를 조정할 수 있지만, 업로드될 때 이미지 자체를 resizing 하는 방법이 있음
- `django-imagekit` 라이브러리 활용

```python
pip install django-imagekit
pip freeze > requirements.txt

# settings.py
INSTALLED_APPS = [
    ...
    'imagekit',
    ...
]
```

- 원본 이미지를 재가공해서 저장 (원본 X, 썸네일 O)

```python
# models.py
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbmail

class Article(models.Model):
    ...
    image = ProcessedImageField(
    	blank=True,
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality': 90},
    )
    ...
   	# ProcessedImageField()의 parameter로 작성된 값들은 변경이 되더라도 	   다시 makemigrations` 해줄 필요 없이 즉시 반영 됨
```

