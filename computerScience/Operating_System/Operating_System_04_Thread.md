# Operating System 04 | Thread

### Thread

- A thread or lightweight process is a basic unit of CPU utilization
- Thread의 구성
  - Program Counter
  - Register set
  - Stack space
- Thread가 동료 thread와 공유하는 부분 = task
  - code section
  - data section
  - OS resources
- 전통적인 개념의 heavyweight process는 하나의 thread를 가지고 있는 task라고 할 수 있음

- 특징
  - 다중 스레드로 구성된 태스크 구조에서는 하나의 서버 스레드가 blocked(waiting) 상태인 동안에도 동일한 태스크 내의 다른 스레드가 실행(running)되어 빠른 처리를 할 수 있음
  - 동일한 일을 수행하는 다중 스레드가 협력하여 높은 처리율(throughput)과 성능 향상을 얻을 수 있음
  - 스레드를 사용하면 **병렬성**을 높일 수 있음
- 장점
  - Responsiveness
    - Multi-threaded Web
  - Resource Sharing
  - Economy
  - Utilization of MP(Multi Processor) Architectures
    - 병렬적으로 running이 가능함

<br>

#### Thread의 구현

- Kernel Threads
  - 커널의 지원을 받음
- User Threads
  - 커널의 지원을 받지 않고, 사용자 수준 (library)의 지원을 받음
- Real-time Threads

<br>

> 본 내용은 이화여자대학교 반효경 교수님 운영체제 강의 내용입니다.
>
> [운영체제 | 이화여자대학교 반효경](http://www.kocw.net/home/search/kemView.do?kemId=1046323)

