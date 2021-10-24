# Django | Model Relationship Ⅱ

### 목차

>- 1:N 관계 설정
>  - User - Article
>  - User - Comment

<br>

### User - Article (1:N)

##### User 모델 참조하기

- `settings.AUTH_USER_MODEL`
  - User 모델에 대한 FK 또는 M:N 관계를 정의할 때 사용해야 함
  - `models.py` 에서 User 모델을 참조할 때 사용
- `get_user_model()`
  - 현재 활성화(active)된 User 모델을 반환
    - 커스터마이징한 User 모델이 있는 경우 Custom User 모델, 그렇지 않으면 기존 내장 User 모델을 반환
    - User를 직접 참조하지 않는 이유
      - 변수 처리를 통해 코드 관리의 용이성 확보
  - `models.py` 가 아닌 다른 모든 곳에서 User 모델을 참조할 때 사용

##### User - Article 간 모델 관계 정의 후 migration

```python
# articles/models.py

from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

##### 게시글 출력 필드 수정

- 게시글 작성 페이지에서 불필요한 필드(`User`)가 출력된다.
  - 사용자 입장에서, 현재 게시글을 작성하는 User = 자신이다. User 필드를 선택할 필요가 없음

- `ArticleForm` 의 출력 필드 수정

```python 
# articles/forms.py

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ('title', 'content',)
```

##### CREATE

- 게시글 작성시 작성자 정보(`article.user`) 추가 후 게시글 작성

```python 
# articles/views.py

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
```

##### UPDATE / DELETE

- 자신이 작성한 게시글만 수정/삭제 가능하도록 설정

```python
# 수정
@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
	else:
        return redirect('articles:index')
    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)

# 삭제
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
		if request.user == article.user:
	    article.delete()
        return redireect('articles:index')
	return redirect('articles:detail', article.pk)
```

##### READ

- 게시글 작성 user가 누구인지 출력
- 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 처리

```django
<!-- articles/index.html -->
...
{% for article in articles %}
	<p><b>작성자 : {{ article.user }}</b></p>
...
```

```django
<!-- articles/detail.html -->

{% if user == article.user %}
	<a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
	<form action="{% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
	</form>
{% endif %}
```

<br>

### User - Comment (1:N)

##### User - Comment 간 모델 관계 정의 후 migration

```python
# articles/models.py

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

##### 댓글 출력 필드 수정

- 게시글 작성 페이지 내의 댓글 작성 Form에서 불필요한 필드(`User`)가 출력됨
  - 게시글 작성 때와 마찬가지로 사용자 입장에서, 현재 댓글을 작성하는 User = 자신이다. User 필드를 선택할 필요가 없음
- 댓글 작성시 `user` ForeignKeyField를 출력하지 않도록 설정

```python 
# articles/forms.py

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ('article', 'user',)
```

- 댓글 작성시 작성자 정보(`request.user`) 추가 후 댓글 작성

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
            comment.user = request.user # 현재 댓글 작성중인 사용자 정보를 추가
            comment.save()
        return redirect('articles:detail', article.pk)
    ...
```

##### READ

- 비로그인 유저에게는 댓글 Form 출력 숨기기

```django
<!-- articles/detail.html -->

{% if request.user.is_authenticated %}
	<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
        {% csrf_token %}
        {{ comment_form }}
        <input type="submit">
	</form>
{% else %}
	<a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인하세요.]</a>
{% endif %}
```

##### DELETE

- 자신이 작성한 댓글만 삭제할 수 있도록 수정

```dtd
<!-- articles/detail.html -->

{% for comment in comments %}
	<li>
	{{ comment.user }} - {{ comment.content }}
    {% if user == comment.user %}
		<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
			{% csrf_token %}
<input type="submit" value="DELETE">
		</form>
	</li>
	{% endif %}
```

```python
# articles/views.py

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```

