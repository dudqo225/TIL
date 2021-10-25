# Django | Model Relationship Ⅲ

### 목차

>- ManyToManyField
>   - 좋아요 기능 (Like)
>   - Profile Page
>   - 팔로우 기능 (Follow)

<br>

### ManyToManyField

##### 개념 및 특징

- 다대다 (M:N, many-to-many) 관계 설정시 사용하는 모델 필드
- M:N 관계로 설정할 모델 클래스가 필수 위치인자로 필요함
- 메서드
  - `add()`
  - `remove()`
  - `create()`
  - `clear()`
  - ...

##### Arguments

- `related_name`
  - target model(관계 필드를 가지지 않은 모델)이 source model(관계 필드를 가진 모델)을 참조할 때(**역참조**) 사용할 Manager의 이름을 설정
  - `ForeignKey`의 `related_name`과 동일
- `through`
  - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 django 모델을 지정할 수 있음
  - 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우에 주로 사용됨
- `symmetrical`
  - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
  - `symmetrical=True` 기본값일 경우, django는 매니저를 추가하지 않음
  - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면, target 모델의 인스턴스도 source 모델의 인스턴스를 자동으로 참조하도록 함
    - 내가 팔로우하면 상대방도 자동으로 팔로우됨
    - 싸이월드에서 일촌맺기와 같은 개념
    - 대칭을 원하지 않는 경우 `False`로 설정

##### Related Manager

- 1:N 혹은 M:N 관계에서 사용되는 매니저
- 같은 이름의 메서드여도 각 관계에 따라 다르게 사용되고 동작한다
  - 1:N 에서는 target 모델 인스턴스만 사용 가능
  - M:N 에서는 관련된 두 객체에서 모두 사용 가능
- 메서드
  - `add()`
    - 지정된 객체를 관련 객체 집합에 추가
    - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
    - 모델 인스턴스, 필드값(PK)을 인자로 허용
  - `remove()`
    - 관련 객체 집합에서 지정된 모델 객체를 제거
    - 내부적으로 `QuerySet.delete()`를 사용하여 관계가 삭제됨
    - 모델 인스턴스, 필드값(PK)을 인자로 허용
  - `create()`
  - `clear()`
  - `set()`
  - ...

##### 중개 테이블의 필드 생성 규칙

- source model과 target model이 다른 경우
  - `id`
  - `<containing_model>_id`
  - `<other_model>_id`
- ManyToManyField 가 동일한 모델을 가리키는 경우
  - `id`
  - `from_<model>_id`
  - `to_<model>_id`

<br>

#### Like

- ManyToManyField 작성

```python
# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

'''
related_name 추가

like_users 필드 생성시 자동으로 역참조는 .article_set 매니저를 생성한다. 그러나 이미 1:N(User:Article) 관계에서 이미 해당 매니저 이름을 사용하기 때문에 related_name을 설정해서 중복을 피해서 에러 발생을 막아야 함.
'''
```

- url 작성

```python
# articles/urls.py

urlpatterns = [
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

- view 함수 작성

```python
# articles/views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
	return redirect('accounts:login')
```

- templates 작성

```django
<!-- articles/index.html -->

...
<form action="{% url 'articles:likes' article.pk %}" method="POST">
    {% csrf_token %}
    {% if user in article.like_users.all %}
    	<input type="submit" value="좋아요 취소">
    {% else %}
    	<input type="submit" value="좋아요">
    {% endif %}
</form>
...
```

<br>

##### 현재 User - Article 간 사용 가능한 DB API

- `article.user`
  - 게시글을 작성한 유저 - 1:N
- `user.article_set`
  - 유저가 작성한 게시글 (역참조) - 1:N
- `article.like_users`
  - 게시글을 좋아요한 유저 - M:N
- `user.like_articles`
  - 유저가 좋아요한 게시글 (역참조) - M:N

<br>

#### Profile Page

- url 작성

```python
# accounts/urls.py

urlpatterns = [
    path('<username>/', views.profile, name='profile'),
]
```

- view 함수 작성

```python
# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

- 프로필 페이지 작성 (template)

```django
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>

<hr>

<h2>{{ person.username }}'s 게시글</h2>
{% for article in person.article_set.all %}
	<div>{{ article.title }}</div>
{% endfor %}

<hr>

<h2>{{ person.username }}'s 댓글</h2>
{% for comment in person.cooment_set.all %}
	<div>{{ comment.content }}</div>
{% endfor %}
<hr>

<h2>{{ person.username }}'s 좋아요한 게시글</h2>
{% for article in person.like_articles.all %}
	<div>{{ article.title }}</div>
{% endfor %}

<hr>

{% endblock %}
```

<br>

#### Follow

- ManyToManyField 작성

```python
# accounts/models.py

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

- url 작성

```python
# accounts/urls.py

urlpatterns = [
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

- view 함수 작성

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
	return redirect('accounts:login')
```

- 프로필 페이지에 팔로우/언팔로우 버튼 작성

```django
<!-- accounts/profile.html -->

<div>
    팔로잉: {{ person.followings.all|length }} / 팔로워: {{ person.followers.all|length }}
</div>
{% if user != person %}
	<form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if user in person.followers.all %}
        	<input type="submit" value="Unfollow">
        {% else %}
        	<input type="submit" value="Follow">
        {% endif %}
	</form>
{% endif %}
```

