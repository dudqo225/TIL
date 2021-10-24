# Django | Model Relationship Ⅰ

### 목차

>- Foreign Key
>    - Comment CREATE
>    - Comment READ
>    - Comment DELETE
>- Customizing Authentication in Django
>    - Substituting a Custom User Model
>    - Custom User & Built-In Auth Forms

<br>

### Foreign Key

##### Foreign Key 개념

- 외래 키 (외부 키)
- 관계형 데이터베이스 (RDB)에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블에서 1개의 키(속성 또는 속성의 집합)에 해당하고, 이 키는 참조되는 테이블의 기본 키(Primary Key)를 가리킨다.
- 참조하는 테이블 행 1개의 값은, 참조되는 테이블의 행 값에 대응됨
- 참조하는 테이블의 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음

##### 특징

- 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
- 외래 키의 값이 반드시 부모 테이블의 PK일 필요는 없지만 유일한 값이어야 함
- 참조 무결성이란?
  - DB 관계 모델에서 관련된 2개의 테이블 간의 일관성
  - 외래 키가 선언된 테이블의 외래키 속성(열)의 값은 부모 테이블의 기본키 값으로 존재해야 한다.

##### FK field

- Many to One relationship
- 2개의 위치 인자가 반드시 필요함
  - 참조하는 *model class*
  - `on_delete`
- migrate 작업 시 필드 이름에 `_id` 가 추가되어 DB 열 이름을 만든다.
- 참고 - 재귀 관계 (자신과 1:N일 때)
  - `model.ForeignKey('self', on_delete=models.CASCADE)`

<br>

##### Comment 모델 정의하기

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # content
    # created_at ...
 	
    def __str__(self):
        return self.content
```

- `on_delete` 인자
  - 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리할 것인지를 정의
  - DB Integrity(데이터 무결성)을 위해서 매우 중요한 설정임
  - 사용 가능한 값들
    - `CASCADE` : 부모 객체가 삭제 되었을 때 이를 참조하는 객체도 삭제 (대부분의 경우에 사용)
    - `PROTECT`, `SET_NULL`, `SET_DEFAULT`, `SET()`, `DO_NOTHING`, `RESTRICT` ...



##### 데이터 무결성

- 데이터의 정확성과 일관성을 유지하고 보증하는 것을 가리키며, DB나 RDBMS 시스템의 중요한 기능이다.
- 무결성 제한의 유형
  - 개체 무결성 (Entity Integrity)
    - PK 개념과 관련
    - 모든 테이블이 PK를 가져야 하며 PK로 선택된 열은 고유한 값이어야 하고, 빈 값은 허용하지 않음을 규정
  - 참조 무결성 (Referential Integrity)
    - FK 개념과 관련
    - FK 값이 데이터베이스의 특정 테이블의 PK 값을 참조하는 것
  - 범위(도메인) 무결성 (Domain Integrity)
    - 정의된 형식(범위)에서 관계형 데이터베이스의 모든 컬럼이 선언되도록 규정



##### 1:N 관계 Related Manager

- 역참조 (`comment_set`)
  - Article (1) → Comment (N)
  - `article.comment` 형태로 사용할 수 없고, `article.comment_set` 이라는 Manager가 생성됨
  - 게시글에 몇 개의 댓글이 작성되었는지 django ORM이 보장할 수 없기 때문
    - 하나의 article에는 comment가 있을 수도 있으나, 없을 수도 있다
    - *실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않다.*
- 참조 (`article`)
  - Comment (N) → Article (1)
  - 댓글(Comment)의 경우 반드시 자신이 참조하고 있는 게시글(Article)이 있으므로,  `comment.article` 과 같이 접근할 수 있음
  - `ForeignKeyField`가 Comment 클래스에 작성되어 있다.



##### related_name 인자

- 역참조 시 사용할 이름('model set' manager)을 변경할 수 있는 옵션

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
```

- 위와 같이 `related_name` 을 작성하면 `article.comment_set`은 사용할 수 없고, `article.comments` 로 대체됨
- 역참조 시 사용할 이름을 수정하고 나면, 반드시 migration 과정이 필요하다.

<br>

#### Comment CREATE

- `CommentForm` 작성

```python
# articles/forms.py

from .models import Article, Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ('article',)

'''
exclude 작성 이유

fields = '__all__' 로 작성하게 되면 detail 페이지에서 CommentForm을 출력할 때 ForeignKeyField를 작성자가 직접 입력해야 하는 상황이 발생한다. (사용자 입장에서는 당연히 지금 내가 보고 있는 Article에 댓글을 작성하는 것인데, 굳이 어떤 Article에 댓글을 작성할 것인지 선택할 필요가 없음)
따라서, CommentForm에서 외래키 필드의 출력을 제외시킨다.
'''
```

- detail 페이지에서 `CommentForm` 출력

```python
# articles/views.py

from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

- 댓글 작성 로직 작성

```python
# articles/urls.py

urlpatterns = [
    path('<int:pk>/comments/', views.comment_create, name='comments_create'),
]
```

```django
<!-- articles/detail.html -->

<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
</form>
```

```python
# articles/views.py

@require_POST
def comments_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)

'''
save() 메서드에서 `commit=False` 작성 이유

아직 DB에 저장되지 않은 인스턴스를 반환 (임시저장의 느낌). 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용.
위 예시에서는 Comment를 저장하기 전에 현재 작성하는 댓글과 연결되는 Article을 저장하는 작업을 수행.
'''
```

<br>

#### Comment READ

- 댓글 출력

```python 
# articles/views.py

from .models import Article, Comment

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm() # 댓글 작성 폼
    comments = article.comment_set.all() # 작성된 댓글 전부 불러오기
    context = {
        'article': article, 
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

- detail 페이지에서 댓글 출력하기

```dtd
<!-- articles/detail.html -->

...

{% for comment in comments %}
	<li>{{ comment.content }}</li>
{% endfor %}
...
```

<br>

#### Comment DELETE

- 댓글 삭제 로직

```python
# articles/urls.py

urlpatterns = [
    path('<int:article_pk>/comments/<int:commen_pk>/delete/', views.comments_delete, name='comments_delete'),
]
```

```python
# articles/views.py

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

```dtd
<!-- articles/detail.html -->

...
<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
</form>
...
```



##### 인증된 사용자의 경우에만 댓글 작성 및 삭제 가능

```python
# articles/views.py

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)
```

<br>

#### Comment 추가사항

- 댓글 갯수 출력하기

```python 
# 1. {{ comments|length }}
# 2. {{ article.comment_set.all|length }}
# 3. {{ comments.count }}
```

- 댓글이 없는 경우

```dtd
<!-- DTL의 for-emtpy 태그 활용-->

{% for comment in comments %}
 {{ comment.content }}

{% empty %}
	<p>댓글이 없어요...</p>

{% endfor %}
```

<br>

### Customizing Authentication in Django

#### Substituting a Custom User Model

- 일부 프로젝트에서는 django의 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있다.
  - ex. username 대신 email을 식별 토큰으로 사용하는 것이 더 적합한 사이트
- django는 User 모델을 참조하는데 사용하는 **`AUTH_USER_MODEL`** 값을 제공하여, 기본 내장 User 모델을 재정의(override) 할 수 있도록 함
- django는 새 프로젝트를 시작할 경우 기본 사용자 모델이 충분하더라도, Custom User Model을 설정하는 것을 강력하게 권장함
- *프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함*

##### AUTH_USER_MODEL

- User를 나타내는데 사용하는 모델
- 프로젝트가 진행되는 동안 변경 불가
- 프로젝트 시작시 설정하기 위한 것이고, 참조하는 모델은 첫번째 Migration에서 사용할 수 있어야 한다.
- 기본값 : `auth.User` (auth 앱의 User 모델)
- 프로젝트 중간에 AUTH_USER_MODEL 변경하기
  - 모델 관계에 영향을 미치기 때문에 어려운 작업이 필요
  - 가능하지만, 중간 변경을 권장하지 않으므로 초기에 설정하자!

##### Custom User 모델 정의하기

- 관리자 권한 + 완전한 기능을 갖춘 User 모델을 구현하는 기본 클래스 `AbstractUser` 를 상속받아서 새로운 User 모델 작성

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

- 기본 django가 사용하는 auth 앱의 User 모델을 accounts 앱의 User 모델을 사용하도록 변경

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

- admin site에 Custom User 모델 등록

```python
# accounts/admin.py
    
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

- 모델 정의 후 마이그레이션 진행

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br>

#### Custom User & Built-In Auth Forms

- 회원가입 시도 시 에러 발생 (`AttributeError`)
  - `UserCreationForm` 과 `UserChangeForm` 은 기존의 django 내장 User 모델을 사용한 ModelForm 이기 때문에 Custom User 모델로 대체해야 함

- 커스텀 User 모델이 `AbstractUser`의 하위 클래스인 경우 아래와 같은 방식으로 form을 확장

```python
# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('custom_field',)
```

- `get_user_model()`
  - 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환
    - User 모델을 커스터마이징한 상황에서는 Custom User 모델을 반환
  - `django.contrib.auth.get_user_model()`을 사용해서 USer 클래스를 참조해야 함