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


#### REST

- **RE**presentational **S**tat **T**ransfer
- API Server를 개발하기 위한 일종의 SW 설계 방법론
- 네트워크 구조 (Network Architecture) 원리의 모음
  - 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
- REST 원리를 따르는 시스템을 RESTful 이란 용어로 지칭
  - RESTful services, simply REST services라고 부름
  - 프로그래밍을 통해서 클라이언트의 요청에 JSON을 응답하는 서버를 구성

- 자원과 주소의 지정 방법
  - 자원
    - URI
  - 행위
    - HTTP Method (GET, POST, PUT, DELETE, etc.)
  - 표현
    - 자원과 행위를 통해 궁극적으로 표현되는 추상화된 결과물
    - JSON으로 표현된 데이터를 제공

##### JSON

- JavaScript Object Notation
- JavaScript의 표기법을 따른 단순 문자열
- 사람이 읽고 쓰기 쉬우며, 기계가 파싱(해석, 분석)하고 만들어내기 쉽다
- 파이썬의 dictionary, 자바스크립트의 object처럼 C 계열 언어가 가지고 있는 자료구조로 `key-value` 형태로 이루어져 있음

<br>

### Response

#### 처리 방법

1. HTML을 응답하는 서버

2. `JsonResponse`

   - JsonResponse 객체를 활용한 JSON 데이터 응답

   ```
   from django.http.response import JsonResponse
   
   def article_json_1(request):
       articles = Article.objects.all()
       articles_json = []
       
       for article in articles:
           articles_json.append(
           	{
                   'id': aritlce.pk,
                   'title': article.title,
                   'content': article.content,
                   ...
               }
           )
       return JsonResponse(articles_json, safe=False)
   ```

   - JsonResponse objects
     - JSON-encoded response를 만드는 HttpResponse의 서브 클래스
     - `safe` parameter
       - True (기본값)
       - dict 이외의 객체를 직렬화(Serialization) 하려면 False로 설정해야 함

#### Serialization

- 직렬화
- 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- **Serializers in Django**
  - QuerySet이나 Model Instance 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어 준다.

3. Django Serializer

   - Django 내장 HttpResponse를 활용한 JSON 응답
   - 주어진 모델 정보를 활용하기 때문에 필드를 개별적으로 직접 만들어줄 필요 X.

   ```python
   from django.http.response import HttpResponse
   from django.core import serializers
   
   def article_json_2(request):
       articles = Article.objects.all()
       data = serializers.serialize('json', articles)
       return HttpResponse(data, content_type='application/json')
   ```

<br>

#### 4. Django REST Framework

- Django REST framework (DRF) 라이브러리를 사용한 JSON 응답
- 설치

```bash
$ pip install djangorestframework
```

```python
# settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

- Article 모델에 맞춰서 자동으로 필드를 생성해 serialize 해주는 ModelSerializer 확인

```python
#  articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
```

- DRF `Response()`를 활용하여 Serialize 된 JSON 객체 응답

```python
# articles/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

<br>

##### DRF

- Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리
- DRF의 Serializer는 django의 Form / ModelForm 클래스와 유사하게 구성되고 작동한다.



##### Django ModelForm vs. DRF Serializers

|          | DJango    | DRF         |
| -------- | --------- | ----------- |
| Response | HTML      | JSON        |
| Model    | ModelForm | serializers |

<br>

### Single Model

- 단일 모델의 CRUD 로직을 수행 가능하도록 설계
- Postman 활용
  - API를 구축하고 사용하기 위해 여러 도구를 제공하는 API 플랫폼
  - 설계, 테스트, 문서화 등의 도구를 제공함으로써 API를 더 빠르게 개발하고 생성할 수 있도록 도움

- Init Project
  - 가상환경 설정 및 패키지 설치
  - 설치된 app 확인 (`settings.py`)
  - `urls.py` 확인
  - `models.py` 확인 - Article 모델 생성
- ModelSerializer
  - 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut
  - 기능
    - 모델 정보에 맞춰 자동으로 필드 생성
    - serializer에 대한 유효성 검사기를 자동으로 생성
    - `.create()` / `.update()` 의 간단한 기본 구현이 포함됨

```python
# articles/serializers.py

'''
Model 필드를 어떻게 직렬화(Serialize)할지 설정하는 것이 핵심
django에서 Model의 필드를 설정하는 것과 동일
'''

from rest_framework import serializers
from .models import Article

classs ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title',)
```

##### many argument

- `many=True`
  - Serializing Multiple Objects
  - 단일 인스턴스 대신 QuerySet 등을 직렬화하기 위해서 serializer를 인스턴스화 할 때, `many=True`를 키워드 인자로 전달해야 함



#### Build RESTful API

|                              | GET                          | POST    | PUT     | DELETE  |
| ---------------------------- | ---------------------------- | ------- | ------- | ------- |
| articles/                    | 전체 글 조회                 | 글 작성 |         |         |
| articles/\<int:article_pk\>/ | \<int:article_pk\>번 글 조회 |         | 글 수정 | 글 삭제 |



#### 1. GET - Article List

- url 및 view 함수 작성

```python
# articles/urls.py

urlpatterns = [
    path('articles/', views.article_list),
]
```

```python
# articles/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, get_list_or_404

from .models import Article
from .serializers import ArticleListSerializer

@api_view(['GET'])
def article_list(request):
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
```

- `api_view` 데코레이터
  - 기본적으로 GET 메서드만 허용됨
  - 다른 메서드 요청에 대해서는 **405 Method Not Allowed** 로 응답
  - View 함수가 응답해야 하는 HTTP 메서드의 목록을 *리스트* 인자로 받음
  - DRF에서는 **필수적으로 작성**해야 해당 view 함수가 정상적으로 동작함



#### 2. GET - Article Detail

- Article List와 Article Detail을 구분하기 위해 추가 Serializer 정의

```python
# articles/serializers.py

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
```

- url 및 view 함수 작성

```python
# articles/urls.py

urlpatterns = [
    path('articles/<int:article_pk>/', views.article_detail),
]
```

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, get_object_or_404

from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
```



#### 3. POST - Create Article

- 201 Created 상태 코드 및 메시지 응답
- RESTful 구조에 맞게 작성
  - URI는 자원을 표현
  - 행위는 HTTP Method
- `aritlce_list` 함수로 게시글을 조회하거나 생성하는 행위 모두 처리 가능

```python
# articles/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render, get_list_or_404

from .models import Article
from .serializers import ArticleListSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    # 게시글 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

##### Status Codes in DRF

- DRF에는 status code를 보다 명확하고 일기 쉽게 만드는데 사용할 수 있는 정의된 상수 집합을 제공
- `status` 모듈에 HTTP status code 집합이 모두 포함되어 있음
-  `status=201` 같은 표현으로 사용할 수 있지만 권장하지 않음

##### 'raise_exception' argument

- `is_valid()`는 유효성 검사 오류가 있는 경우 serializers.ValidationError 예외를 발생시키는 `raise_exception` 인자를 사용할 수 있음
- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며, HTTP status code 400을 응답으로 반환함.



#### 4. DELETE - Delete Article

- 204 No Content 상태 코드 및 메시지 응답
- `article_detail` 함수로 상세 게시글 조회/삭제 행위 모두 처리 가능

```python
# articles/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, get_object_or_404

from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
```



#### 5. PUT - Update Article

- `article_detail` 함수로 상세 게시글 조회/삭제/수정 행위 모두 처리 가능

```python
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    ...
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        # serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

<br>

### 1:N Relation

- Comment 모델 작성

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    ...
```



#### 1. GET - Comment List

- CommentSerializer 작성

```python
# articles/serializers.py

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
```

- url 작성 및 comment_list 함수 정의

```python
# articles/urls.py

urlpatterns = [
    path('comments/', views.comment_list),
]
```

```python
# articles/views.py

from .models import Comment
from .serializers import CommentSerializer

@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
```



#### 2. GET - Comment Detail

- url 작성 및 comment_detail 함수 정의

```python
# articles/urls.py

urlpatterns = [
    path('comments/<int:comment_pk>/', views.comment_detail),
]
```

```python
# articles/views.py

@api_view(['GET'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
```



#### 3. POST - Create Comment

- url 작성 및 comment_create 함수 작성

```python
# articles/urls.py

urlpatterns = [
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
```

```python
# articles/views.py

@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
	    return Response(serializer.data, status=status.HTTP_201_CREATED)
```

##### .save()

- `.save()` 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
- 인스턴스를 저장하는 시점에 추가 데이터 삽입이 필요한 경우

##### Read Only Field (읽기 전용 필드)

- 어떤 게시글에 작성하는 댓글인지에 대한 정보를 form-data로 넘겨주지 않았기 때문에 직렬화 과정에서 유효성 검사를 통과하지 못함
- 읽기 전용 필드 설정을 통해 직렬화하지 않고 반환 값에만 해당 필드가 포함되도록 설정할 수 있음

```python
# articles/serializers.py

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
```



#### 4. DELETE & PUT - delete, update Comment

- comment_detail 함수가 모두 처리할 수 있도록 작성

```python
# views.py

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=reqeust.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```



#### 1:N Serializer

- 특정 게시글에 작성된 댓글 목록 출력하기
  - 기존 필드 override
- 특정 게시글에 작성된 댓글 개수 구하기
  - 새로운 필드 추가

##### 1. 특정 게시글에 작성된 댓글 목록 출력하기

- Serializer는 기존 필드를 override 하거나 추가 필드를 구성할 수 있음

- 2가지 형태로 구성 가능

  - PrimaryKeyRelatedField

    - pk를 사용하여 관계된 대상을 나타냄
    - 필드가 many relationships(N)를 나타내는데 사용되는 경우 `many=True` 속성 필요
    - comment_set 필드값을 form-data로 받지 않으므로 `read_only=True` 설정 필요

    ```python
    # serializers.py
    
    class ArticleSerializer(serializers.ModelSerializer):
        comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        
        class Meta():
            model = Article
            fields = '__all__'
    ```

    ```python
    # articles/models.py
    
    '''
    역참조시 생성되는 comment_set을 override 할 수 있음
    '''
    
    class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    ```

  - Nested Relationships

    - 모델 관계상 참조된 대상은 참조하는 대상의 표현(응답)에 포함되거나 중첩될 수 있음
    - 중첩된 관계를 serializers 필드로 사용하여 표현 가능
    - 두 클래스의 위치를 변경해야 함

    ```python
    # serializers.py
    
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
            read_only_fields = ('article',)
            
    class ArticleSerializer(serializers.ModelSerializer):
        comment_set = CommentSerializer(many=True, read_only=True)
        
        class Meta():
            model = Article
            fields = '__all__'
    ```



##### 2. 특정 게시글에 작성된 댓글 개수 구하기

- 기존에는 `comment_set` 매니저는 모델 관계로 인하여 자동 구성되기 때문에 커스텀 필드를 작성하지 않아도 comment_set이라는 필드명을 fields 옵션에 작성만해도 사용할 수 있음
- But, 별도의 값을 위한 필드를 사용하려는 경우 자동으로 구성되는 매니저가 아니기 때문에 필드를 직접 작성해야 함

```python
# articles/serializers.py

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta():
        model = Article
        fields = '__all__'
```

##### source argument

- 필드를 채우는데 사용할 속성의 이름
- 점 표기법(dot notation)을 사용하여 속성을 탐색할 수 있음
- `comment_set` 이라는 필드에 `.`(dot)을 통해 전체 댓글 개수 확인 가능
- `.count()`는 built-in QuerySet API 중 하나

##### read_only_fields shortcut issue

- 특정 필드를 override 하거나 추가한 경우 `read_only_fields` shortcut으로 사용할 수 없음

```python
# articles/serializers.py

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count')
    
    class Meta():
        model = Article
        fields = '__all__'
        read_only_fields = ('comment_set', 'comment_count',)
        # 위와 같이는 사용 불가
```

