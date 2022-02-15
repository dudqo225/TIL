# Operating System 01 | Overview

### OS란?

- 컴퓨터 하드웨어 바로 위에 설치되어 사용자 및 다른 소프트웨어 ↔ 하드웨어 사이를 연결하는 소프트웨어 계층

<br>

#### 목표

- 컴퓨터 시스템을 편리하게 사용할 수 있는 환경을 제공
- HW를 직접 다루는 복잡한 부분을 OS가 대행
- 컴퓨터 시스템의 **자원을 효율적으로 관리**

<br>

#### 분류

- 동시 작업 가능 여부
  - 단일 작업(single tasking)
    - MS-DOS
  - 다중 작업(multi tasking)
    - UNIX, MS Windows

- 사용자의 수
  - 단일 사용자(single user)
    - MS-DOS, MS Windows
  - 다중 사용자(multi user)
    - UNIX, NT server
- 처리 방식
  - 일괄 처리 (batch porcessing)
    - 작업 요청을 일정량 모아서 한꺼번에 처리
    - 작업이 완전 종료될 때까지 기다려야 함
  - 시분할 (time sharing)
    - 컴퓨터 처리 능력을 일정한 시간 단위로 분할해서 여러 작업을 수행
    - 짧은 응답 시간을 가짐
    - interactive한 방식
    - 대부분 시분할 OS이다. (윈도우, iOS 등...)
  - 실시간 (real-time)
    - 정해진 시간 안에 어떠한 일이 반드시 종료됨이 보장되어야 하는 시스템을 위한 OS
    - ex. 원자로/공장 제어, 미사일 제어, 반도체 장비, 로보트 제어
    - 개념 확장
      - Hard realtime system(경성 실시간 시스템)
      - Soft realtime system(연성 실시간 시스템)

<br>

#### 용어

- Multitasking
- Multiprogramming
- Time Sharing
- Multiprocess
  - 위 용어들은 컴퓨터에서 여러 작업을 동시에 수행하는 것을 뜻함
  - Multiprogramming은 여러 프로그램이 메모리에 올라가 있음을 강조
  - Time Sharing은 CPU의 시간을 분할해서 나눠쓴다는 의미를 강조
  - ※ Multiprocessor : 하나의 컴퓨터에 CPU(processor, 처리기)가 여러개 붙어있음을 의미

<br>

#### OS 예시

- 유닉스 (UNIX)
  - 대부분 C언어로 작성
  - 높은 이식성
  - 최소한의 커널 구조
  - 복잡한 시스템에 맞게 확장이 용이
  - 소스 코드 공개
  - 프로그램 개발에 용이
  - 다양한 버전
    - System V, FreeBSD, SunOS, Solaris
    - Linux
- MS
  - DOS (Disk Operating System)
    - 1981년 IBM-PC를 위해 개발
    - 단일 사용자용 OS, 메모리 관리 능력의 한계 (주 기억 장치: 640KB)
  - Windows
    - 다중 작업용 GUI 기반 OS
    - Plug and Play, 네트워크 환경 강화
    - DOS용 응용 프로그램과 호환성 제공
    - 초창기에는 불안정성 존재
    - 풍부한 지원 SW

<br>

#### 구조

- CPU → CPU 스케쥴링
- Memory → 메모리 관리
- Disk → 파일 관리
- I/O Device → 입출력 관리

- Software → 프로세스 관리

<br>

> 본 내용은 이화여자대학교 반효경 교수님 운영체제 강의 내용입니다.
>
> [운영체제 | 이화여자대학교 반효경](http://www.kocw.net/home/search/kemView.do?kemId=1046323)

