# Django | Form

### 목차

> - Form Class
> - ModelForm
> - Rendering fields manually
> - Handling HTTP requests

<br>

### 1. Form Class

#### Intro

- HTML form, input을 통해 사용자로부터 데이터를 받았다.
- 이렇게 직접 입력 받으면 데이터의 유효성을 검증하고, 필요시 입력된 데이터를 검증 결과와 함께 다시 표시하는 등 많은 노력이 필요하다.
- **Django Form** 은 일부 과중한 작업과 반복 코드를 줄여줌으로써, 이러한 작업을 쉽게 만들어 줌.

<br>

#### Django's forms

- Form은 유효성 검사 도구들 중 하나이고, 공격 및 우연한 데이터 손상에 대한 중요한 방어수단
- Django form은 form 기능의 방대한 부분을 단순하고 자동화할 수 있으며, 프로그래머가 직접 작성한 코드에서 수행할 수 있는 것보다 더 안전하게 수행 가능.
- Form에 관련된 작업 세 부분을 처리
  - 렌더링을 위한 데이터 준비 및 재구성
  - 데이터에 대한 HTML fomrs 생성
  - 클라이언트로부터 받은 데이터 수신 및 처리

- `Form Class`
  - Django Form 관리 시스템의 핵심
  - form 내부 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관련된 에러 메시지를 결정
  - 데이터 유효성 검증, 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등의 과중한 작업과 반복 코드를 줄여줌

<br>

##### Form 선언하기

- Model을 선언하는 것과 유사. 같은 필드타입을 사용(일부 매개변수도 유사)
- `forms` 라이브러리에서 파생된 `Form` 클래스를 상속받음

##### Rendering Options

- <label> & <input> 쌍에 대한 3가지 옵션
  - `as_p()` 
    - 각 필드가 단락. `<p>` 태그로 감싸져서 렌더링 됨
  - `as_ul()`
    - 각 필드가 목록. `<li>` 태그로 감싸져서 렌더링 됨
    - `<ul>` 태그는 직접 작성해야 함
  - `as_table()`
    - 각 필드가 테이블. `<tr>` 태그로 감싸져서 렌더링 됨
    - `<table>` 태그는 직접 작성해야 함

##### Django의 HTML input 요소 표현 방법 2가지

- Form fields

  - **input에 대한 유효성 검사 로직을 처리**하며 템플릿에서 직접 사용 됨

- Widgets

  - 웹 페이지의 HTML input 요소 렌더링
  - GET/POST 딕셔너리에서 데이터 추출
  - 반드시 form fields에 할당되어야 함
  - vs. Form Fields 단순 raw한 렌더링 처리

  ```python
  # 예시
  content = forms.CharField(widget=forms.Textarea)
  ```

<br>

### 2. ModelForm

#### Intro

- Article 모델이 있고 사용자가 게시글을 제출할 수 있는 양식을 만들고 싶은 경우, 이미 모델에서 필드를 정의했기 때문에 form에서 필드를 재정의하는 중복된 행위 발생
- Django는 Model을 통해 Form Class를 만들 수 있는 Helper 제공
  - `ModelForm`

#### ModelForm Class

- Model을 통해 Form Class를 만들 수 있는 Helper
- 일반 Form Class와 완전히 같은 방식(객체를 생성)으로 view에서 사용 가능

#### ModelForm 선언하기

```python
# articles/forms.py 

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'   # Article 모델의 모든 필드를 불러오기
        exclude = ('title',) # 제외할 항목 설정
```

- forms 라이브러리에서 파생된 `ModelForm` 클래스를 상속받음
- 정의한 클래스 내부에 `Meta` 클래스를 선언, 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 `Meta` 클래스에 지정

##### Meta Class

- `Model`의 정보를 작성하는 곳
- `ModelForm` 을 사용할 경우 사용할 모델이 있어야 한다. 이를 `Meta` 클래스가 구성함.
  - 해당 `model`에서 정의한 `field`  정보를 Form 에 적용
- 참고
  - Inner class (Nested class)
    - 클래스 내에 선언된 다른 클래스
    - 관련 클래스를 함께 그룹화 하여 가독성 및 프로그램 유지 관리를 지원 (노리적으로 묶어서 표현)
    - 외부에서 내부 클래스에 접근할 수 없으므로 코드 복잡성을 줄일 수 있음
  - Meta Data
    - 데이터에 대한 데이터

##### is_valid() Method

- 데이터 유효성 검사를 보장하기 위한 많은 테스터들에 대해 django는 `is_valid()`를 제공
- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 `boolean` 값으로 반환
- 참고
  - 유효성 검사
    - 요청한 데이터가 특정 조건에 충족하는지 확인하는 작업
    - 데이터베이스 각 필드 조건에 올바르지 않은 데이터가 서버로 전송되거나, 저장되지 않도록 하는 것

##### save() Method

- form에 바인딩 된 데이터에서 DB 객체를 만들고 저장
- ModelForm의 하위 클래스는 기존 모델 인스턴스를 키워드 인자 `instance` 로 받아들일 수 있음
  - 제공되면 save()는 해당 인스턴스를 UPDATE
  - 제공되지 않으면 save()는 지정된 모델의 새 인스턴스를 CREATE
- form의 유효성이 확인되지 않은 경우 (hasn't been validated)
  - save()를 호출하면 form.errors를 확인하여 에러 확인이 가능

##### widgets 적용하기

- django의 HTML input element 표현

- HTML 렌더링을 처리

- 방식

  - 첫 번째

  ```python
  class ArticleForm(forms.ModelForm):
      
      class Meta():
          model = Article
          fields = '__all__'
          widgets = {
              'title': forms.TextInput(attrs={
                  'class': 'title',
                  'placeholder': 'Enter the title',
                  'maxlength': 10,
              	}
              )    
          }
  ```

  - 두 번째 (권장)

  ```python
  class ArticleForm(forms.ModelForm):
      title = forms.CharField(
      	label='제목',
      	widget=forms.TextInput(
          	attrs={
                  'class': 'my-title',
                  'placeholder': 'Enter the title',
              }
          )
      )
      
      class Meta():
          model = Article
          fields = '__all__'    
  ```

<br>

#### Form & ModelForm

- Form
  - 어떤 model에 저장해야 하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너리를 생성
  - cleaned_data 딕셔너리에서 데이터를 가져온 후 `.save()`를 호출
  - `model` 에 연관되지 않은 데이터를 받을 때 사용
- ModelForm
  - django가 해당 model에서 양식에 필요한 대부분의 정보를 미리 정의
  - 어떤 레코드를 만들어야 할지 알고 있으므로 바로 `.save()` 호출 가능
- **ModelForm 이 Form 의 진화, 발전 버전이 아니다**. 상황에 따라서 둘 다 사용하는 것.

<br>

### 3. Rendering fields manually

- 수동으로 Form 작성

  - Rendering fields manually
  - Looping over the form's fields - `{% for  %}`

- Bootstrap과 함께 사용

  - Bootstrap class with widgets

    - Bootstrap Form Class
      - 핵심 클래스 : `form-control`
      - 핵심 클래스를 widget에 작성
      - 에러 메시지 with bootstrap alert component

  - Django Bootstrap 5 Library

    - django-bootstrap v5

      - form class에 bootstrap을 적용시켜주는 라이브러리

      ```bash
      pip install django-bootstrap-v5
      
      # 설치 이후 PJT settings.py에 적용
      INSTALLED_APPS = [
      	...
      	'bootstrap5',
      	...
      ]
      ```

      - 적용

      ```python
      {% load bootstrap5 %}
      	...
      	{% bootstrap_css %}
      	...
      	{% bootstrap_javascript %}
      ```

<br>

### 4. Handling HTTP requests

- django에서 HTTP 요청을 처리하는 방법
  - django shortcut functions
  - View Decorators

##### django shortcuts functions

- `django.shortcuts` 패키지는 개발에 도움되는 여러 함수 및 클래스 제공
- 종류
  - `render()`
  - `redirect()`
  - `get_object_or_404()`
    - 모델 manager `objects` 에서 `get()` 을 호출하지만, 해당하는 객체가 없을 경우 `DoesNotExist` 예외 대신 **HTTP 404** 호출
    - `get()` 메서드의 경우
      - 조건에 맞는 데이터가 없으면 에러를 발생시킴
      - 코드 실행 단계에서 발생한 에러에 대해 브라우저는 **http status code 500 으로 인식**함
    - 상황에 따라 적절한 예외처리를 하고 클라이언트에게 올바른 에러를 전달하는 것 또한 개발의 중요 요소 중 하나
  - `get_list_or_404()`

<br>

##### django View decorators

- django는 다양한 HTTP 기능을 지원하기 위해 뷰에 적용할 수 있는 여러 데코레이터를 제공
- Decorator 란?
  - 어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 연장해주는 함수

- `Allowed HTTP methods`
  - 요청 메서드에 따라 view 함수에 대한 엑세스 반환
  - 요청이 조건을 충족시키지 못하면 HttpResponseNotAllowed 를 반환 (405 Method Not Allowed)
  - 종류
    - `require_http_methods()`
      - view 함수가 특정한 method 요청에 대해서만 허용하도록 하는 데코레이터
    - `require_POST()`
      - view 함수가 POST method 요청만 승인하도록 하는 데코레이터
    - `require_safe()`, ~~`require_GET()`~~

- *HTTP 요청에 따라 적절한 예외처리 및 데코레이터를 통해 서버를 보호하고 클라이언트에게 정확한 상황을 제공하는 것이 중요하다!*

