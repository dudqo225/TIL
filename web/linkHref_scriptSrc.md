# HTML & CSS | \<link href> & \<script src>  차이

- Bootstrap을 활용할 때 CSS 파일은 \<link href> 태그에 JS 파일은 \<script src> 태그에 작성하여 활용하게 된다.
- `CDN` 을 사용하여 파일 불러오기를 할 때도 CSS와 JS를 가져오는 태그는 다르다.

</br></br>

> 왜 달라? 😮

</br></br>

#### \<link href>

- HTML의 `<link`> 요소는 현재 문서와 외부 리소스 간의 관계를 명시한다.
- 주로 HTML `<head`> 가 끝나기 직전에 코드를 작성한다.
- 스타일 시트를 연결할 때 제일 많이 사용.
- **파비콘, 홈화면 아이콘을 연결할 때**도 사용할 수 있다.

- `rel` 은 관계 (relationship) 를 뜻하며, 현재 문서와 연결한 아이템의 관계를 설명한다.

```html
# CSS 연결할 때
<link href="main.css" rel="stylesheet">

# 파비콘 연결할 때
<link rel="icon" href="favicon.ico">
```

- `media` 특성을 사용하여 특정 미디어 조건을 만족할 때 리소스를 불러올 수 있음

```html
<link href="print.css" rel="stylesheet" media="print">
<link href="mobile.css" rel="stylesheet" media="screen and (max-width: 600px)">
```

- 간단히 정리하면,
  - 현재 HTML과 외부 style.css를 연결하여 style.css 에 정의된 스타일을 현재 HTML에 사용한다는 의미

</br></br>

#### \<script src>

- HTML `<script`> 요소는 데이터와 실행가능한 코드를 문서에 포함할 때 사용하며 보통 `JavaScript` 코드와 함께 사용한다.

```html
# JavaScript 코드를 사용하고자 할 때
<script type="text/javascript" src="https://code.js"></script>
```

- HTML `<body>` 가  끝나는 전 부분에 코드를 작성한다.

</br></br>

#### 차이점

- `href` 와 `src` 의 차이를 이해하면 된다.
- `href` 는 브라우저에서 HTML 파일을 불러오는 것과 `href` 링크 파일을 가져오는 것을 동시에 (병렬) 처리
- `src` 는 `src`에 링크된 파일을 가져오는 동안 브라우저가 페이지를 불러오는 것을 일시 중단한다.
- `href` 와 `src` 가 파일을 불러오고 HTML 문서를 읽는 방식에서 차이가 있기 때문에
-  `<link` 태그는 `<head>` 가 끝나는 부분, `<script`> 는 `<body>` 가 끝나는 부분에 작성하는 것이다.
- 예를 들어,
  - `<script`> 를 `<head>` 에서 불러오게끔 코드를 작성하면,
  - 코드를 불러오는 과정에서 브라우저는 HTML 문서 읽기를 일시중단 하기 때문에
  - 사용자 입장에서 브라우저 화면에 콘텐츠가 없는 것 처럼 보일 수 있다.
  - 그러면 이탈 하겠지? (마케팅 시각에서..)

</br></br>

> **참고 사이트**
>
> [steemit | \<link href> 와 \<script src>](https://steemit.com/javascript/@beerntv/link-href-script-src)
>
> [MDN | \<link>: 외부 리소스 연결 요소](https://developer.mozilla.org/ko/docs/Web/HTML/Element/link)
>
> [MDN | \<script>: 스크립트 요소](https://developer.mozilla.org/ko/docs/Web/HTML/Element/script)

