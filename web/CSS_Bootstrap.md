# CSS | Bootstrap

### Bootstrap

- The most popular HTML, CSS, and JS library in the world

- 트위터에서 시작된 오픈 소스 프론트엔드 라이브러리

- 웹페이지에 쓰이는 요소 거의 전부를 내장

- 별도의 디자인 시간이 ↓ . 다양한 웹브라우저 지원을 위한 크로스 브라우징에 불필요한 시간을 사용하지 않도록 함

- one source - multi use

  - 반응형 웹 디자인

- CDN (Content Delivery(Distribution) Network)

  - 콘텐츠(CSS, JS, Image, Text 등)를 효율적으로 전달하기 위해 여러 노드를 가진 네트워크에 데이터를 제공하는 시스템.
  - 서버와 사용자 사이의 물리적 거리를 줄여 콘텐츠 로드 지연을 최소화
  - 분산된 서버로 이루어진 플랫폼
    - 전세계 사용자들이 로딩 시간을 늦추지 않고 동일한 품질의 콘텐츠 사용이 가능
  - 장점
    - 사용자와 가까운 서버를 통해 빠르게 전달이 가능
    - 외부 서버를 활용하기 때문에 본인 서버의 부하가 적어진다

- Spacing

  |  m   | margin  |
  | :--: | :-----: |
  |  p   | padding |

  |     t     |     top      |
  | :-------: | :----------: |
  |     b     |    bottom    |
  | s (start) |     left     |
  |  e (end)  |    right     |
  |     x     | left & right |
  |     y     | top & bottom |

  |  0   |  0 rem   | 0px  |
  | :--: | :------: | :--: |
  |  1   | 0.25 rem | 4px  |
  |  2   | 0.5 rem  | 8px  |
  |  3   |  1 rem   | 16px |
  |  4   | 1.5 rem  | 24px |
  |  5   |  3 rem   | 48px |

- Responsive Web

  - 다양한 화면 크기를 가진 디바이스들이 등장하면서 개념이 등자
  - 별도의 기술이름이 아닌, 웹 디자인에 대한 접근 방식.
  - 반응형 레이아웃 작성에 도움이 되는 사례들의 모음을 기술하는데 사용되는 용어
  - 예시
    - Media Queries, Flexbox, Bootstrap Grid System, The viewport meta tag

</br></br>

### Bootstrap Grid System

- CSS flexbox 로 제작됨
- `container`, `rows`, `column` 으로 콘텐츠를 배치하고 정렬
- **12개의 `column` 과 6개의 `grid breakpoints` 로 구성되어 있음!**
- Grid System class
  - row
    - columns 의 wrapper
  - gutters
    - 반응적으로 공간을 확보하고 콘텐츠를 정렬하는데 사용
    - column 사이의 padding
  - col, col-*
    - row 당 가능한 12개 중 사용하려는 columns 수를 나타냄
    - 너비는 백분율로 설정. 부모 요소를 기준으로 유동적으로 크기가 조정됨
    - 반드시 columns 안에 있어야 하며 row의 바로 하위 자식으로 있을 수 있다
  - offset
    - 지정한 만큼 column 공간을 무시하고 다음 공간부터 콘텐츠 적용
  - Nesting (중첩)
    - row > col-* > row > col-* 방식으로 중첩 사용 가능
- Grid breakpoints
  - 다양한 디바이스에서 적용하기 위해 특정 px 에 대한 지점을 정해 둔 것을 breakpoints 라고 함
  - bootstrap 에서는 크기 정의를 대부분 em / rem 으로 하지만, px 은 grid breakpoint 에 사용
    - viewport 너비가 픽셀단위이고 글꼴 크기에 따라 변하지 않기 때문