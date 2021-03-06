# WEB | 싸피 메이트 PJT 회고

지난 6주간 참여했던 프로젝트에 대한 회고글을 작성하려고 한다. 따라서 이 글은 개발 개념이나 기술에 관한 것이 아니다. 6주간 진행했던 프로젝트에서 느꼈던 점이나 다음 프로젝트에서 보완 개선할 내용 등에 대해서 서술한다.

<br>

### 프로젝트 개요

##### 서비스명

- 싸피 메이트 (SSAFY MATE)

<br>

#####  일정

- 2022.01.04 ~ 2022.02.18

<br>

##### 기획 및 목적

- 삼성청년소프트웨어아카데미 2학기 프로젝트 과정에서 팀빌딩을 원활하게 하기 위함.
- 공통/특화/자율 프로젝트 등 총 3번의 프로젝트를 진행하는데, 싸피 교육생 간 프로필 확인 및 보유 기술 스택 등을 확인하여 좀 더 쉽게 팀을 구성할 수 있다.

<br>

### PJT 회고

6주간 서비스를 개발하면서 정말 많이 성장했다고 생각한다. 물론 아직 갈 길이 한참 멀긴하지만, 스스로 모르는 내용이나 우리 서비스에 필요한 개념들을 공부하고 적용해보는 시간이었다. 또한, 내가 어떤 부분을 더 보완하고 개선해야 되는지에 대해서도 배울 수 있는 유익한 기간이었다.

<br>

##### 성장한 부분

- Java 언어와 Spring Boot 프레임워크를 사용해보면서 **새로운 언어/기술을 습득**할 수 있었다.
- MySQL, H2, Redis 등 **다양한 DB를 사용**해볼 수 있었다. 
  - 관계형, 비관계형, 메모리 기반 DB 등 다양한 것을 사용함
- **RESTful API**에 대해서 다시한번 개념 정립 및 개발
  - 1학기 관통프로젝트에서 Python - Django를 사용하여 RESTful API를 만들었었다. 그 경험을 살려서 다른 언어/프레임워크를 활용하여 우리 서비스에 맞는 API 서버를 개발하였다. 기술은 달라도 RESTful 하다는 개념은 동일하기 때문에 지난 학기에서 이해가지 않았던 부분이나 부족했던 부분을 보완하면서 개발할 수 있었다.
- **SMTP** 통신으로 이메일 인증 구현, **Spring Security, JWT** 활용하여 인증 구현
  - 조금 생소하지만 중요한 개념이었다. 직접 부딪히고 공부하면서 우리 서비스에 맞게 구현할 수 있었다.
- **Convention** 작성 및 적용
  - Git 작성을 위한 컨벤션과 더불어 코드 컨벤션을 작성하여 팀원 간 공유하였다. 이 과정이 있었기 때문에 팀원 간 코드 및 문서의 통일성을 어느정도 지킬 수 있었다.
  - 팀원이 6명이나 되는 개발과정이 처음이었기 때문에 컨벤션을 작성하고 적용하는 과정이 매우 유익했다.
- **배포 과정**을 경험함
  - 가장 소중한 경험이었다고 생각한다. AWS EC2 인프라 환경 구축, 프론트 / 백 API 서버 / 백 채팅 서버 배포, GitHub Webhook과 Jenkins 연동, Docker를 활용하여 이미지 생성 및 컨테이너 띄우기, Nginx 웹서버 연결 등 처음해보는 부분이었다.
  - 하지만 직접 내가 역할을 맡아서 진행하면서 가장 많이 배울 수 있었던 부분이라고 생각한다.
  - 이제 막 시작한 단계이지만 **배포**의 영역도 지속적으로 공부해야 겠다.
- **실사용자** 받기
  - 우리 서비스의 주요 타겟층은 싸피 교육생이다. 
  - 남들보다 개발 일정을 앞당겨서 배포하고, 도메인을 구입하여 사용자의 유입을 용이하게 하였다.
  - 배포한 약 10일의 기간동안 싸피 교육생 **170**명이 우리 서비스에 가입하였다. 또한 Github Issue 탭에 버그, 이슈 리포팅을 해준 교육생도 있다.
  - 오픈 채팅, 구글 폼 등을 통해 의견을 받았고 즉각적으로 대응하면서 실제 서비스 운영에 대해서 경험해볼 수 있었다.

<br>

##### 보완 / 개선할 부분

- **코드 리팩토링**
  - 혼자 작업하면서도 코드의 개선이 필요했으나, 협업을 하면서 코드 리팩토링이 정말 필요하다는 생각을 많이 했다. 개발자 성향에 따라서 코드 작성 스타일이 다르기 때문에 코드 컨벤션을 명확하게 하여 우리 서비스의 코드가 통일성을 유지하도록 해야한다.
- **테스트**
  - 프로젝트 기획 단계에서 JUnit을 활용하여 테스트를 진행하자고 했었다. 하지만 실제로 개발을 진행하면서 전혀 활용해보지 못한 것이 아쉽다.
  - 실제 개발한 API들은 Swagger와 Postman을 사용하여 테스트를 진행하였다. 하지만, 무수히 많은 테스트를 반복하면서 효율성이 떨어졌다. 다음 프로젝트에서는 단위, 통합 테스트 등을 진행하기 위해서 JUnit과 같은 기술을 사용해봐야겠다.
- **소통** 많이 하기
  - 정말 다행스러운 것은 우리 팀은 프로젝트를 진행하면서 싸우지 않았다는 것이다. 물론 의견을 나누고 맞춰가는 과정에서 삐걱거림이 없었다고는 할 수 없다. 하지만 팀원들 모두가 양보하고 상대방을 인정하려는 자세가 있었기 때문에 서비스를 완성하고 프로젝트를 무사히 마칠 수 있었다.
  - 하지만 좀 더 소통을 많이 할 걸... 이라는 아쉬움은 남는다. 분명 내 의견을 좀 더 피력하지 못했던 적이 많다. ""내 말이 맞아!" 가 아닌, "난 이렇게 생각하는데 어때?" 라는 말을 좀 더 하고 내 의견을 어필했으면 더 좋았을 것이다.

<br>

### 마무리

아쉬움과 후련함이 공존한 프로젝트였다. 프론트엔드 친구들이 훌륭해서 다른 팀보다 훌륭한 서비스 화면, 기능을 구현할 수 있었다. 백엔드 친구들이 함께 해주어 어려웠지만 DB 설계, API 개발, 배포 등의 과정을 진행할 수 있었다. 실제 사용자를 받아서 서비스 운영을 경험해볼 수 있었다. 

<br>

좋은 팀원들을 만나 좋은 서비스를 기획, 개발, 배포하고 운영할 수 있는 정말 좋은 시간이었다.

<br>

하지만 완벽한 개발, 서비스란 세상에 없기 때문에 여기서 만족하지는 않겠다. 나 또한 완벽한 개발자가 아니고 이제 막 시작한 주니어 개발자이기 때문에 더더욱 성장하기 위해 매일매일 노력할 것이다.

<br>

**하루에 한걸음씩! 꾸준히 성장하는 개발자 손영배입니다 :D** 라는 슬로건을 지키기 위해 노력하자!

##### 