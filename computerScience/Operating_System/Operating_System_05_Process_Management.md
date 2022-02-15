# Operating System 05 | Process Management

### 프로세스의 생성 (Process Creation)

- Copy-on-write (COW)
- 부모 프로세스가 자식 프로세스를 생성 (복제 생성- 문맥(context)을 그대로 복사)
- 프로세스의 트리(계층 구조) 형성
- 프로세스는 자원을 필요로 함
  - OS로부터 받음
  - 부모와 공유

- 자원의 공유
  - 부모와 자식이 모든 자원을 공유하는 모델
  - 일부를 공유하는 모델
  - 전혀 공유하지 않는 모델
- 수행 (Execution)
  - 부모와 자식은 공존하며 수행되는 모델
  - 자식이 종료(terminate)될 때까지 부모가 기다리는(wait) 모델
- 주소 공간 (Address Space)
  - 자식은 부모의 공간을 복사 (binary and OS data)
  - 자식은 그 공간에 새로운 프로그램을 올림
- ex. 유닉스
  - `fork()` 시스템 콜이 새로운 프로세스를 생성
    - 부모를 그대로 복사 (OS data except PID + binary)
    - 주소 공간을 할당
  - fork 다음에 이어지는 `exec()` 시스템 콜을 통해서 새로운 프로그램을 메모리에 올림

<br>

### 프로세스 종료 (Process Termination)

- 프로세스가 마지막 명령을 수행한 후 OS에게 이를 알려줌 (exit)
  - 자식이 부모에게 output data를 보냄 (wait)
  - 프로세스의 각종 자원들이 OS에게 반납됨
- 부모 프로세스가 자식의 수행을 종료시킴 (abort)
  - 자식이 할당 자원의 한계치를 넘어섬
  - 자식에게 할당된 태스크가 더 이상 필요하지 않음
  - 부모가 종료(exit)되어야 하는 경우
    - OS는 부모 프로세스가 종료하는 경우 자식이 더 이상 수행되도록 두지 않음
    - 단계적인 종료

<br>

### fork() 시스템 콜

- create a child (copy)
- 프로세스는 `fork()` 시스템 콜에 의해서 생성됨
- 중복 생성

```c
int main()
{	int pid;
 	pid = fork();
 	if (pid == 0)
     	printf('\n Hello, I am child!\n');
 	else if (pid > 0)
     	printf('\n Hello, I am parent!\n'); 
}
```

<br>

### exec() 시스템 콜

- overlay new image
- `exec()` 시스템 콜에 의해서 새로운 프로그램을 실행시킴
- 메모리에 새로운 프로그램을 올림

```c
int main()
{	int pid;
 	pid = fork();
 	if (pid == 0)
    { 	printf('\n Hello, I am child! Now I'll run date \n');
        execlp("/bin/date", "/bin/date", (char*)0);
    }
 	else if (pid > 0)
     	printf('\n Hello, I am parent!\n'); 
}
```

<br>

### wait() 시스템 콜

- sleep until child is done
- 프로세스 A가 `wait()` 시스템 콜을 호출하면
  - 커널은 child가 종료될 때까지 프로세스 A를 sleep 시킨다 (block 상태)
  - Child process가 종료되면 커널은 프로세스 A를 깨운다 (ready 상태)

<br>

### exit() 시스템 콜

- frees all the resources and notify parent
- 프로세스의 종료
  - 자발적 종료
    - 마지막 statement 수행 후 exit() 시스템 콜을 통해
    - 프로그램에 명시적으로 적어주지 않아도 main 함수가 리턴되는 위치에 컴파일러가 넣어줌
  - 비자발적 종료
    - 부모 프로세스가 자식 프로세스를 강제로 종료시킴
      - 자식 프로세스가 한계치를 넘어서는 자원을 요청하는 경우
      - 자식에게 할당된 태스크가 더 이상 필요하지 않을 경우
    - 키보드로 kill, break 등을 친 경우
    - 부모가 종료되는 경우
      - 부모 프로세스가 종료되기 전에 자식들이 먼저 종료됨

<br>

### 프로세스 간 협력

- 독립적 프로세스 (Independent process)
  - 프로세스는 각자의 주소 공간을 가지고 수행되므로 원칙적으로 하나의 프로세스는 다른 프로세스의 수행에 영향을 미치지 못함
- 협력 프로세스 (Cooperating process)
  - 프로세스 협력 메커니즘을 통해서 하나의 프로세스가 다른 프로세스의 수행에 영향을 미칠 수 있음
- 프로세스 간 협력 메커니즘(IPC - InterProcess Communication)
  - 메시지를 전달하는 방법
    - message passing : 커널을 통해서 메시지를 전달
  - 주소 공간을 공유하는 방법
    - shared memory
      - 서로 다른 프로세스 간에 일부 주소 공간을 공유
    - thread
      - 쓰레드는 하나의 프로세스이므로 프로세스 간 협력이라고 보기 어렵지만, 동일한 process를 구성하는 쓰레드들 간에는 주소 공간을 공유하므로 협력의 개념으로 볼 수 있음

##### Message Passing

- Message system
  - 프로세스 사이에 공유 변수(shared variable)를 일체 사용하지 않고 통신하는 시스템
- 종류
  - Direct Communication
    - 통신하려는 프로세스의 이름을 명시적으로 표시
  - Indirect Communication
    - mailbox 혹은 port를 통해서 메시지를 간접적으로 전달

<br>

### 프로세스의 특성 분류

- I/O bound process
  - CPU를 잡고 계산하는 시간보다 I/O에 많은 시간이 필요한 job
  - many short CPU bursts
- CPU bound process
  - 계산 위주의 job
  - few very long CPU bursts

<br>

> 본 내용은 이화여자대학교 반효경 교수님 운영체제 강의 내용입니다.
>
> [운영체제 | 이화여자대학교 반효경](http://www.kocw.net/home/search/kemView.do?kemId=1046323)

