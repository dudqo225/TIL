

# Operating System 운영체제

- Operating System 운영체제란?

  - 시스템 하드웨어를 관리할 뿐 아니라,

  - 응용 소프트웨어를 실행하기 위해 하드웨어 추상화 플랫폼과 공통 시스템 서비스를 제공하는 **시스템 소프트웨어**이다.

  - 최근에는 가상화 기술의 발전으로, 실제 하드웨어가 아닌 하이퍼 바이저(가상머신) 위에서 실행되기도 함.

  - 응용 프로그램과 하드웨어 사이의 **중재자** 역할

    ![Operating system placement kor.png](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Operating_system_placement_kor.png/180px-Operating_system_placement_kor.png)

  - 실행되는 응용 프로그램들이 메모리 / CPU / 입출력 장치 등의 자원을 사용할 수 있도록 만들어 주고, 이들을 *추상화* 하여 파일 시스템 등의 서비스를 제공

  - 대표적인 운영체제

    - Windows
    - Mac OSX
    - Linux
    - iOS

</br></br>

### 운영체제의 목적

- 컴퓨터의 하드웨어를 관리 (Performance)
  - CPU, 메모리, 디스크, 키보드, 마우스, 모니터, 네트워크 등의 하드웨어를 잘 관리해야 컴퓨터를 효율적으로 사용할 수 있음
  - 운영체제의 성능이 좋을수록 컴퓨터의 성능이 좋아진다고 할 수 있음
- 사용자에게 편의를 제공 (Convenience)
  - OS가 없다면 하드웨어에 관한 모든 관리를 사용자가 해야 함
  - 컴퓨터를 사용하는데 불편함을 겪을 수 있음

</br></br>

#### 부팅 (Booting)

- Booting
  - 컴퓨터 전원이 켜지면 프로세서(CPU) 에서 ROM에 있는 내용을 읽는다.
  - ROM 안에는 POST(Power-On Self-Test)와 Boot loader가 저장되어 있다.
    - POST는 전원이 켜지면 가장 먼저 실행되는 프로그램으로 현재 컴퓨터의 상태를 검사
    - POST 작업 이후, Boot loader가 실행됨.
  - Boot loader 는 하드디스크에 저장되어 있는 OS를 찾아서 RAM(메인 메모리)에 가져온다.

![img](https://user-images.githubusercontent.com/34755287/53879648-5b041180-4052-11e9-9642-6bf80de33a3e.png)

- 용어 정리
  - Processor : 일반적으로 CPU를 의미한다.
  - Main Memory
    - ROM : 비휘발성. 메모리에서 극히 일부를 차지
    - RAM. 휘발성. 메모리의 대부분을 차지하고, 실제 프로그램이 할당되는 곳
  - Kernel : 커널. 운영체제가 수행하는 모든 것이 저장되어 있는 곳.
  - Shell : 명령어 해석기 (Command interpreter). 사용자가 커널에 요청하는 명령어를 해석하여 커널에 요청하고 그 결과를 출력한다.

</br></br>

### 운영 체제 분류

- 동시 작업 가능여부
  - Single Tasking (MS-DOS)
  - Multi-Tasking
- 사용자 수
  - Single user
  - Multi user
- 처리 방식
  - Batch processing
    - 일괄처리 방식. 여러 작업을 한꺼번에 모아서 처리
  - Time sharing
    - 컴퓨터 능력을 일정 시간으로 쪼개서, 여러 프로그램에 할당한다.
    - 응답속도가 빠르며, 데드라인이 없음.
    - 현대의 일반적인 컴퓨터에 사용됨.
  - Realtime OS
    - 데드라인이 존재하기 때문에, 그 시간 안에 처리가 되어야 한다.
      - Hard Realtime System (시간을 잘 지키는)
      - Soft Realtime System (시간을 대강 지키는)

</br></br>

### 운영체제 구조

- CPU 
  - 어떤 프로그램에게 CPU를 할당할지 판단 - CPU 스케쥴링
- 메모리
  - 한정된 메모리를 어떻게 쪼개서 할당할지 판단 - 메모리 관리
- 디스크
  - 디스크에 파일을 어떻게 보관할지 판단 - 파일 관리
- 입출력장치
  - 각기 다른 입출력 장치와 컴퓨터 간에 어떻게 정보를 주고 받게할지를 결정 - 입출력 관리

- 기타
  - 프로세스 관리, 네트워킹, 보호/보안 등





#### 참고

> https://ko.wikipedia.org/wiki/%EC%9A%B4%EC%98%81_%EC%B2%B4%EC%A0%9C
>
> https://velog.io/@codemcd/%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9COS-1.-%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C%EB%9E%80
>
> https://jisuhan.tistory.com/62
>
> https://qteveryday.tistory.com/3
>
> https://brunch.co.kr/@toughrogrammer/15







