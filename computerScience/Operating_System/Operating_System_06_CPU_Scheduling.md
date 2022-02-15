# Operating System 06 | CPU Scheduling

### CPU scheduler & dispatcher

- CPU scheduler
  - ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고름
- Dispatcher
  - CPU의 제어권을 CPU 스케쥴러에 의해 선택된 프로세스에게 넘긴
  - 이 과정을 context switch(문맥 교환)이라고 함
- CPU 스케쥴링이 필요한 경우
  - Running > Blocked (I/O 요청하는 시스템 콜) -nonpreemptive(강제로 빼앗지 않고 자진 반납)
  - Running > Ready (할당시간 만료로 timer interrupt) - preemptive (강제로 빼앗음)
  - Blocked > Ready (I/O 완료 후 인터럽트) - preemptive
  - Terminate - nonpreemptive

<br>

### Scheduling Criteria

#### Performance Index (= Performance Measure, 성능 척도)

- CPU utillization (이용률)
- Throughput (처리량)
- Turnaround time (소요시간, 반환시간)
- Waiting time (대기 시간)
- Response time (응답 시간)

> 중국집 예시... 월급을 줘서 주방장을 고용한다.
>
> 같은 월급 내에서 주방장이 최대한 일을 하게 시키는 것 > 이용률
>
> 단위 시간당 중국음식을 최대한 많이 만드는 것  > 처리량
>
> 손님이 짜장면, 탕수육 같은 음식을 먹는데 소요되는 시간 > 소요시간, 반환시간
>
> 맛집이라 줄 서서 대기하는 시간 > 대기 시간
>
> 짜장면이 나올 때까지 걸리는 시간 > 응답 시간

<br>

### Scheduling Algorithm

#### 1. FCFS (First-Come First-Served)

- 비선점형 스케쥴링
- 먼저 도착하면 먼저 CPU를 선점한다.
- 먼저 도착하는 프로세스의 소요 시간이 얼마냐에 따라서 평균 대기 시간이 달라진다.
  - `Convoy effect` : 긴 프로세스가 먼저 도착해서 짧은 프로세스들이 오랜 시간 대기하는 현상

#### 2. SJF (Shortest Job-First)

- CPU burst time이 가장 짧은 프로세스를 제일 먼저 스케쥴링하는 것
- 두 가지 Schemes
  - Nonpreemptive
    - 일단 CPU를 잡으면 CPU burst가 완료될 때까지 CPU를 선점(preemption) 당하지 않음
  - Preemptive
    - 현재 수행중인 프로세스의 남은 burst time보다 더 짧은 CPU burst time을 갖는 새로운 프로세스가 도착하면 CPU를 빼앗김
    - Shortest-Remaining-Time-First(SRTF)라고도 부름
- SJF is optimal
  - 주어진 프로세스들에 대해서 최소 평균 대기 시간(minimum average waiting time)을 보장
- 문제점
  - Starvation (기아 현상)
    - CPU 사용시간이 긴 프로세스가 영원히 실행되지 않을 수도 있음
  - CPU 사용시간을 미리 알 수 없음
    - 과거의 CPU burst time을 이용해서 추정(estimate)
    - **Exponential Averaging**

#### 3. Priority Scheduling

- 우선순위가 제일 높은 프로세스에게 CPU를 할당
- SJF는 일종의 priority scheduling
- 문제점
  - Starvation
- 해결방법
  - Aging (노화)
    - 시간이 지나면서 프로세스의 우선순위를 높여주는 것

#### 4. Round Robin (RR)

- 각 프로세스는 동일한 크기의 할당 시간(time quantum)을 가짐 - 일반적으로 10~100 milliseconds
- 할당 시간이 지나면 프로세스는 CPU를 빼앗기고(preempted) ready queue의 제일 뒤에 가서 다시 대기한다.
- n개의 프로세스가  ready queue에 있고 할당 시간이 q time unit인 경우
  - 각 프로세스는 최대 q time unit 단위로 CPU 시간의 1/n을 얻는다.
  - 어떤 프로세스도 (n-1)q time unit 이상 기다리지 않는다.
- Performance
  - q large > FCFS
  - q small > context switch (오버헤드가 커짐)
- 일반적으로 SJF보다 turnaround time은 길지만 response time은 짧다

#### 5. Multilevel Queue

- Ready Queue를 여러개로 분할
  - foreground (interactive)
  - background (batch - no human interaction)
- 각 큐는 독립적인 스케쥴링 알고리즘을 가짐
  - foreground - RR (Round Robin)
  - background - FCFS (First-Come First-Served)
- 큐에 대한 스케쥴링이 필요
  - Fixed priority scheduling
    - forground의 큐들을 먼저 다 serve하고 그 후 background를 serve
    - starvation이 발생할 가능성 있음
  - Time slice
    - 각 큐에 CPU Time을 적절한 비율로 할당
    - ex. 80% to foreground in RR, 20% to background in FCFS

#### 6. Multilevel Feedback Queue

- 프로세스가 다른 큐로 이동이 가능
- Aging을 이와 같은 방식으로 구현 가능
- Multilevel feedback queue scheduler를 정의하는 파라미터
  - Queue의 수
  - 각 큐의 scheduling algorithm
  - 프로세스를 상위 큐로 보내는 기준
  - 프로세스를 하위 큐로 내쫒는 기준
  - 프로세스가 CPU 서비스를 받으려 할 때 들어갈 큐를 정하는 기준

<br>

### Multiple-Processor Scheduling

- CPU가 여러 개인 경우 스케쥴링은 더 복잡해짐
- Homogeneous processor인 경우
  - Queue에 한줄로 세워서 각 프로세서가 알아서 꺼내가게 할 수 있음
  - 반드시 특정 프로세서에서 수행되어야 하는 프로세스가 있는 경우에는 문제가 복잡해진다
- Load Sharing
  - 일부 프로세서에 job이 몰리지 않도록 부하를 적절히 공유하는 메커니즘이 필요
  - 별개의 큐를 두는 방법 or 공동 큐를 사용하는 방법
- Symmetric Multiprocessing (SMP)
  - 각 프로세서가 알아서 스케쥴링을 결정
- Asymmetric Multiprocessing
  - 하나의 프로세서가 시스템 데이터의 접근/공유를 책임지고 나머지 프로세서는 거기에 따름

<br>

### Real-Time Scheduling

- Hard real-time systems
  - task가 정해진 시간 안에 반드시 끝내도록 스케쥴링 해야 함
- Soft real-time systems
  - task가 일반 프로세스에 비해 높은 priority를 갖도록 해야 함

<br>

### Thread Scheduling

- Local Scheduling
  - User level thread의 경우 사용자 수준의 thread library에 의해 어떤 thread를 스케쥴할지 결정
- Global Scheduling
  - Kernel level thread의 경우 일반 프로세스와 마찬가지로 커널의 단기 스케쥴러가 어떤 thread를 스케쥴할지 결정

<br>

### Algorithm Evaluation

- Queueing Models
  - 확률 분포로 주어지는 arrival rate와 service rate 등을 통해 각종 performance index 값을 계산
- Implementation (구현) & Measurement (성능 측정)
  - 실제 시스템에 알고리즘을 구현하여 실제 작업(workload)에 대해서 성능을 측정하고 비교
- Simulation (모의 실험)
  - 알고리즘을 모의 프로그램으로 작성 후 trace를 입력으로 하여 결과를 비교

<br>

> 본 내용은 이화여자대학교 반효경 교수님 운영체제 강의 내용입니다.
>
> [운영체제 | 이화여자대학교 반효경](http://www.kocw.net/home/search/kemView.do?kemId=1046323)

