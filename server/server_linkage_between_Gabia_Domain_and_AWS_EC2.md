# server | Linkage between Gabia Domain and AWS EC2

프로젝트를 진행하면서 가비아에서 도메인을 구입해서 적용하는 과정을 진행했다. 이때, 기존에 Nginx 설정파일에 작성한 몇가지 내용의 수정이 필요했다. 예를 들어, `server_name`이나 `ssl` 인증서 관련 설정을 변경해야 했다.

<br>

### 1. Gabia 도메인

도메인 사이트에서 내가 원하는 도메인을 구입하고 적용하는 일은 크게 어렵지 않다.

**도메인 검색 - 구입 - DNS 레코드 수정**의 과정을 거쳐서 쉽고 빠르게 도메인 적용을 할 수 있다.

<br>

```bash
# 도메인 연결을 위한 퍼블릭 IP 주소 찾기
$ curl ifconfig.me
```

- 도메인 연결을 할 때 AWS EC2 인스턴스의 퍼블릭 IP 주소가 필요하다. EC2 콘솔에서 쉽게 확인할 수 있지만 서버 자체에서 위 명령어를 통해서 퍼블릭 IP 주소를 확인할 수 있다.

<br>

***

<br>

기존의 Nginx `.conf` 파일에는 가비아에서 구매한 도메인이 아닌 EC2 도메인이 설정되어 있어서, 가비아에 구매하고 연결한 도메인으로 접속하면 정상적으로 연결이 되지 않는 문제가 발생했다.

이 문제를 해결하기 위해서

- **certbot** 으로 SSL 인증서 발급받기
- **Nginx** `.conf` 파일 수정하기

두 가지 과정이 필요하다.

<br>

### 2. certbot 설치 및 인증서 발급

##### certbot이란?

![image-20220209140742449](server_linkage_between_Gabia_Domain_and_AWS_EC2.assets/image-20220209140742449.png)

이전에 클라이언트와 서버에 HTTPS 보안 설정을 하기 위해서 **Let's Encrypt** 라는 오픈소스 도구를 사용한 적이 있다. **certbot** 은 Let's Encrypt 인증서를 자동으로 발급 및 갱신해주는 봇 프로그램이다.

우리는 certbot 프로그램을 활용하여 가비아에서 구매한 도메인을 이름으로 하는 SSL 인증서를 발급받을 것이다.

<br>

```bash
$ sudo apt install certbot python3-certbot-nginx
```

명령어를 통해서 certbot 패키지를 설치한다.

<br>

![image-20220209115225200](C:\Users\YB\AppData\Roaming\Typora\typora-user-images\image-20220209115225200.png)

명령어가 정상적으로 동작한다면 위 이미지와 같이 설치가 진행될 것이다.

<br>

```bash
$ sudo certbot --nginx -d <도메인명> -d <www.도메인명>
```

`-d` 옵션 뒤에 지정할 도메인을 입력한다. 기본 도메인과 더불어 `www` 가 붙은 도메인 총 2개를 입력하였다.

<br>

![image-20220209115254576](C:\Users\YB\AppData\Roaming\Typora\typora-user-images\image-20220209115254576.png)

마찬가지로, 명령어가 동작하면 공개키와 비밀키가 생성된다.

이미지 하단에 오류처럼 보이는 내용은, SSL 인증서 생성 전에 Nginx `.conf` 파일에 `server_name`(서버명) 을 명시하지 않았다는 안내메시지로 인증서 생성에는 영향을 미치지 않는다.

<br>

SSL 인증서 생성이 완료되면, 이전에 보았던 **IMPORTANT NOTES** 메시지를 확인할 수 있다. 이 노트에는 공개키/비밀키 저장 위치와 인증서 만료일자 등의 정보가 표시된다.

![image-20220209115133408](C:\Users\YB\AppData\Roaming\Typora\typora-user-images\image-20220209115133408.png)

<br>

***

<br>

### 3. Nginx .conf 수정

마지막으로 `.conf` 파일을 수정한다. 서버명과 SSL 인증키 저장 위치를 변경해야 한다.

```bash
# 기존 .conf 파일

server {
  listen 80;
  listen [::]:80;

  root /home/ubuntu/ssafy-mate_front-end/build;
  index index.html;
  server_name i6a402.p.ssafy.io;
  
  location / {
    return 301 https://$host$request_uri;
  }
}

server {
  listen 443 ssl;
  listen [::]:443 ssl;
  
  server_name i6a402.p.ssafy.io;
  
  ssl  on;
  ssl_certificate "/etc/letsencrypt/live/i6a402.p.ssafy.io/fullchain.pem";
  ssl_certificate_key "/etc/letsencrypt/live/i6a402.p.ssafy.io/privkey.pem";

  ...
}
```

```bash
# 변경한 .conf 파일

server {
  listen 80;
  listen [::]:80;

  root /home/ubuntu/ssafy-mate_front-end/build;
  index index.html;
  server_name ssafymate.site;
  
  location / {
    return 301 https://$host$request_uri;
  }
}

server {
  listen 443 ssl;
  listen [::]:443 ssl;

  server_name ssafymate.site;

  ssl  on;
  ssl_certificate "/etc/letsencrypt/live/ssafymate.site/fullchain.pem";
  ssl_certificate_key "/etc/letsencrypt/live/ssafymate.site/privkey.pem";

  ...
}
```

- `server_name` 
  - i6a402.p.ssafy.io → ssafymate.site 변경
- `ssl_certificate` & `ssl_certificate_key`
  - 기존 인증서 저장 위치 → 새로 발급받은 인증서 저장 위치 변경

<br>

설정 파일 변경 후 Nginx를 재시작한다.

```bash
$ sudo systemctl reload nginx
```

<br>

가비아 도메인 및 HTTPS 보안까지 잘 적용된 것을 확인할 수 있다!

![image-20220209115402010](C:\Users\YB\AppData\Roaming\Typora\typora-user-images\image-20220209115402010.png)