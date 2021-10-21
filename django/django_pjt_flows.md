# django PJT flows

> 2021.10.21 Instagram 비슷하게 만들기



---

### django 프로젝트 기본 설정

프로젝트를 진행할 최상위 폴더 생성

venv 설정

```python
python -m venv venv
```



django 설치 (필요시 requirements.txt 설치)

```
pip install django
pip install -r requirements.txt
```



django 프로젝트 생성

```
django-admin startproject 프로젝트명 .
```



django 앱 생성

```
python manage.py startapp 앱명
```



앱 등록

- 프로젝트 폴더 > `settings.py` > INSTALLED_APPS 변수 > 생성한 앱 추가



---

### 기본 html 구조 생성

루트 경로에 templates 폴더 생성

templates > base.html 생성(`! Tab`)

bootstrap 추가 홈페이지 CDN



`_nav.html` 생성 > include 하기 위함

```django
{% include '_nav.html' %}
```



`settings.py` > `TEMPLATES` > `DIRS` > `[BASE_DIR / 'templates']` 추가



---

### 프로젝트 폴더 내 앱 url 추가

```python
# 프로젝트 > urls.py
from django.urls import path, include

urlpatterns = [
	path('accounts/', include('accounts.urls')),
	path('articles/', include('articles.urls')),
]
```

```python
# 각 앱 폴더에 urls.py 파일 생성
# accounts 앱
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
]

# articles 앱
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
]
```



---

### User Model 확장

- django 기본 모델이 아닌, 사용자 기반 user 생성이 가능하도록 사전에 확장하는 것.

```python
# accounts > models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
	followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    image = ProcessedImageField(upload_to='avatars',
                                processors=[ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality': 60})
```

- `symmetrical` 옵션
  - 싸이월드, 인스타 following 예시
  - True이면, 맞팔
  - False이면, 일방향 following
  - User 간 팔로잉, 일촌맺기와 같은 다대다 재귀 관계(`self`)에서만 사용
- `settings.py` > `AUTH_USER_MODEL` 추가

```python
AUTH_USER_MODEL = 'accounts.User'
```

- 마이그레이션 진행

```
python manage.py makemigrations
python manage.py migrate
```



---

### Image 사용

- django 기본 이미지 필드가 아닌 라이브러리 사용
  - Pillow 설치
  - `pip install django-imagekit`
  - `imagekit` to `INSTALLED_APPS`

```python
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Profile(models.Model):
    avatar_thumbnail = ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(100, 50)],
                                           format='JPEG',
                                           options={'quality': 60})
```



- 사용자가 이미지를 업로드하는 경로 추가
  - `settings.py` > `MEDIA_ROOT` & `MEDIA_URL` 추가

```python
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
```



---

### accounts

- 회원가입

  - urls.py

  ```python
  # urlpatterns 추가
  path('signup/', views.signup, name='signup'),
  ```

  - views.py

  ```python
  # 구조 생성
  from django.shortcuts import redirect
  
  def signup(request):
      if request.method == 'POST':
          pass
      else:
          pass
  
      return render(request, 'accounts/form.html')
  ```

  - forms.py
    - 기존 django의 `UserCreationForm` 을 상속받은 `CustomUserCreationForm` 생성

  ```python
  # accounts > forms.py 파일 생성
  from django.contrib.auth.forms import UserCreationForm
  from django.contrib.auth import get_user_model
  
  class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm.Meta):
          model = get_user_model()
          fields = UserCreationForm.Meta.fields + ('email', 'image')
  ```

  - views.py

  ```python
  from django.shortcuts import redirect, render
  from .forms import CustomUserCreationForm
  
  def signup(request):
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST, request.FILES)
          if form.is_valid():
              form.save()
              return redirect('accounts:login')
      else:
          form = CustomUserCreationForm()
  
      context = {
          'form': form,
      }
  
      return render(request, 'accounts/form.html', context)
  ```

  - templates
    - form 태그 내부에 파일 입력을 받기 위한 encoding 설정
    - `enctype="multipart/form-data"`

  ```django
  # templates > accounts > form.html
  {% extends 'base.html' %}
  
  {% block body %}
    <form action="" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{ form }}
      <input type="submit">
    </form>
  {% endblock body %}
  ```



##### django bootstrap 5 사용하기

- 설치
  - `pip install django-bootstrap-v5`
- `settings.py` > `INSTALLED_APPS` 에 추가
  - `bootstrap5`
- `form.html` 코드 수정

```django
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block body %}
  <form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {% bootstrap_form form %}
    <input type="submit">
  </form>
{% endblock body %}
```



- 로그인

  - urls.py

  ```python
  path('login/', views.login, name='login'),
  ```

  - views.py

  ```python
  # 구조 생성
  from django.contrib.auth.forms import AuthenticationForm
  from django.contrib.auth import login as auth_login
  
  def login(request):
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              user = form.get_user()
              auth_login(request, user)
              return redirect('accounts:profile', user.username)
  
      else:
          form = AuthenticationForm()
  
      context = {
          'form': form,
      }
      
      return render(request, 'accounts/form.html', context)
  ```

  

- Profile 페이지 생성

  - urls.py

  ```python
  path('<username>/', views.profile, name='profile'),
  ```

  - views.py

  ```python
  from django.shortcuts import get_object_or_404
  from django.contrib.auth import get_user_model
  
  def profile(request, username):
      User = get_user_model()
      
      user = get_object_or_404(User, username=username)
  ```

  - templates

  ```django
  {% extends 'base.html' %}
  
  {% block body %}
    <div class="row">
      <div class="col-3 mt-4">
        <img src="{{ profile_user.image.url}}" alt="" class="border rounded-circle">
      </div>
      <div class="col-9">
        <p>{{ profile_user.username }}</p>
      </div>
    </div>
  {% endblock body %}
  ```

  

##### 이미지 출력을 위한 경로 설정

```python
# 프로젝트 폴더 > urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



---

### articles

- index 페이지

  - urls.py

  ```python
  path('', views.index, name='index'),
  ```

  - views.py

  ```
  def index(request):
      return render(request, 'articles/index.html')
  ```

  - templates

  ```
  {% extends 'base.html' %}
  
  {% block body %}
    <h1>index</h1>
  {% endblock body %}
  ```

  

- Article 모델 생성

  - models.py

  ```python
  # Article
  from django.conf import settings
  from imagekit.models import ProcessedImageField
  from imagekit.processors import ResizeToFill
  
  class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      content = models.TextField()
      image = ProcessedImageField(upload_to='images',
                                  processors=[ResizeToFill(500, 500)],
                                  format='JPEG',
                                  options={'quality': 100})
      like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
      created_at = models.DateTimeField(auto_now_add=True)
  
  # Comment
  class Comment(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.CharField(max_length=50)
  ```

  - 마이그레이션 하기

  ```python
  python manage.py makemigrations
  python manage.py migrate
  ```

  

- 폼 생성

  - forms.py

  ```python
  from django import forms
  from .models import Article, Comment
  
  class ArticleForm(forms.ModelForm):
      class Meta():
          model = Article
          fields = ('content', 'image')
  
  
  class CommentForm(forms.ModelForm):
      class Meta():
          model = Comment
          fields = ('content')
  ```

  

##### settings.AUTH_USER_MODEL vs. get_user_model()

```
settings.AUTH_USER_MODEL은 변수이므로, 단순한 string 값이 들어가 있음

get_user_model()은 인스턴스로 생성가능.
```



- 신규 article 생성

  - urls.py

  ```python
  path('create/', views.create, name='create'),
  ```

  - views.py

  ```python
  # 구조 생성
  # Create
  def create(request):
      if request.method == 'POST':
          pass
      else:
          pass
  
      return render(request, 'articles/form.html')
  ```

  - templates

  ```python
  {% extends 'base.html' %}
  {% load bootstrap5 %}
  
  {% block body %}
    <form action="" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {% bootstrap_form form %}
      <input type="submit">
    </form>
  {% endblock body %}
  ```

  - views.py

  ```python
  from django.shortcuts import redirect, render
  from .models import Article
  from .forms import ArticleForm
  
  # Create
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST, request.FILES)
          if form.is_valid():
              article = form.save(commit=False)
              article.user = request.user
              article.save()
              return redirect('articles:index')
      else:
          form = ArticleForm()
      
      context = {
          'form': form,
      }
  
      return render(request, 'articles/form.html', context)
  ```

  - index 수정

  ```python
  def index(request):
      articles = Article.objects.all()
      context = {
          'articles': articles,
      }
      return render(request, 'articles/index.html', context)
  ```

  ```python
  # _card.html 생성
  # humanize / 게시글 생성자 이미지 넣기 (article.user.image.url)
  {% load humanize %}
  
  <div class="card" style="">
    <img src="{{ article.image.url }}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">
        <img src="{{ article.user.image.url }}" alt="" width="50px" class="border rounded-circle">
        <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a>
      </h5>
      <p class="card-text">{{ article.content }}</p>
      {% comment %} <a href="#" class="btn btn-primary">Go somewhere</a> {% endcomment %}
      <p>{{ article.created_at|naturaltime }}</p>
    </div>
  </div>
  ```

  ```python
  # index.html 수정
  {% extends 'base.html' %}
  
  {% block body %}
    {% for article in articles %}
      <div class="col-7">
        {% include 'articles/_card.html' %}
      </div>
    {% endfor %}
  {% endblock body %}
  ```



- article에 comment 달기

  - views.py

  ```python
  # CommentForm 추가
  
  def index(request):
      articles = Article.objects.all()
      form = CommentForm()
      context = {
          'articles': articles,
          'form': form,
      }
      return render(request, 'articles/index.html', context)
  ```

  - `_card.html`

  ```django
  {% load bootstrap5 %}
  	...
      <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
        {% csrf_token %}
        {% bootstrap_form form show_label=False %}
        <input type="submit" class="btn btn-primary">
      </form>
      ...
  ```

  - urls.py

  ```python
  path('<int:pk>/comments/create/', views.comments_create, name='comments_create'),
  ```

  - views.py

  ```python
  def comments_create(request, pk):
      form = CommentForm(request.POST)
  
      if form.is_valid():
          comment = form.save(commit=False)
          comment.user = request.user
          comment.article_id = pk
          comment.save()
  
          return redirect('articles:index')
  ```

  - _card.html

  ```python
      {% for comment in article.comment_set.all %}
        <p>{{ comment.user }} : {{ comment.content }}</p>
      {% endfor %}
  ```

  

- 좋아요

  - urls.py

  ```python
  path('<int:pk>/likes/', views.likes, name='likes'),
  ```

  - views.py

  ```python
  def likes(request, pk):
      user = request.user
      article = get_object_or_404(Article, pk=pk)
  
      if user in article.like_users.all():
          article.like_users.remove(user)
      else:
          article.like_users.add(user)
      
      return redirect('articles:index')
  ```

  - `_card.html`에 좋아요 버튼 추가 

  ```python
  # JavaScript를 활용하여 좋아요 하트 버튼 표시
  
  <p>
    <form action="{% url 'articles:likes' article.pk %}" method="POST" id="like-form-{{ article.pk }}">
          {% csrf_token %}
    </form>
          {% if user in article.like_users.all %}
            <a href="#" onclick="document.querySelector('#like-form-{{ article.pk }}').submit()"><i class="fas fa-heart" style="color: red"></i></a>
          {% else %}
            <a href="#" onclick="document.querySelector('#like-form-{{ article.pk }}').submit()"><i class="far fa-heart" style="color: black"></i></a>
          {% endif %}
  
        {{ article.like_users.all|length }} 명이 게시물을 좋아합니다.
  </p>
  ```



***

### Navigation



```python
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="{% url 'articles:index' %}"><i class="fab fa-instagram"></i></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
      {% if user.is_authenticated %}
        <li class="nav-item">
          <a class="nav-link" href="{% url 'articles:create' %}">Create</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'accounts:profile' user.username %}">Profile</a>
        </li>
      {% else %}
        <li class="nav-item">
          <a class="nav-link" href="{% url 'accounts:signup' %}">Signup</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'accounts:login' %}">Login</a>
        </li>
      {% endif %}
      </ul>
    </div>
  </div>
</nav>
```



***

### 팔로우 기능



- profile.html

```django
{% if user != profile_user %}
    <form action="{% url 'accounts:follow' profile_user.pk %}" method="POST">
        {% csrf_token %}
        {% if user in profile_user.followers.all %}
        <input type="submit" class="btn btn-primary" value="팔로우 취소">
        {% else %}
        <input type="submit" class="btn btn-primary" value="팔로우">
        {% endif %}
    </form>
{% endif %}

<p>게시물: {{ profile_user.article_set.all|length }} | 팔로워: {{ profile_user.followers.all|length }} | 팔로우: {{ profile_user.followings.all|length }}</p>

<div class="row">
    {% for article in profile_user.article_set.all %}
    <div class="col-4">
        <img src="{{ article.image.url }}" alt="" class="img-fluid">
    </div>
    {% endfor %}
</div>
```

-  urls.py

```python
path('<int:pk>/follow/', views.follow, name='follow'),
```

- views.py

```python
def follow(request, pk):
    User = get_user_model()
    
    me = request.user
    you = get_object_or_404(User, pk=pk)

    if me in you.followers.all():
        # you.followers.remove(me)
        me.followings.remove(you)
    else:
        # you.followers.add(me)
        me.followings.add(you)

    return redirect('accounts:profile', you.username)
```

