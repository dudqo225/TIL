<img src="git.assets/1200px-Git-logo.svg.png" alt="초보자를 위한 깃(Git) 사용법 · Yoon&#39;s devlog" style="zoom:25%;" />



### git 이란?

- **(분산) 버전 관리 시스템** - **DVCS**(**D**istributed **V**ersion **C**ontrol **S**ystem)
- 코드의 History를 관리하는 도구.
- 개발된 과정과 역사를 볼 수 있으며, 프로젝트 이전 버전을 복원하고 변경 사항을 비교, 분석 및 병합이 가능
- **차이(diff)** 가 무엇이고, 수정 이유를 log로 남길 수 있다.



- **리누스 토발즈**가 개발 (리룩스의 창시자)

<img src="git.assets/R800x0" alt="리누스 토발즈(Linus Torvalds)와 Open Source 진영 ... 그리고, 욕" style="zoom: 50%;" />

<center>👍 대단한 사람이다!!!</center>

***



### git_command

> git 기본 명령어 정리



#### 생성

- **`init`** : 로컬 저장소 설정.
  - 현재 폴더를 git으로 관리 하겠다.
  - 현재 폴더에 `.git` 폴더를 생성
  - **최초 1회만 실행**하는 명령어
  - PJT 단위에서 실행

```bash
git init
```



- **Author(작성자) 설정**
  - `user.name` : 사용자명
  - `user.email` : 이메일 주소 (GitHub 계정과 일치)

```bash
git config --global user.name <사용자명>
git config --global user.email <이메일 주소>

git config --global -l # git 설정 확인
```



#### 확인

- `status` : 상태 확인
  - 현재 git이 관리하고 있는 파일들의 상태를 보여주는 명령어

```bash
git status
```



- `log` : 커밋의 히스토리를 보여주는 명령어

```bash
git log
```



#### 관리

##### 1) 로컬 관리

- **`add`** : 커밋할 목록에 추가
  - Working Directory에서 Staging Area에 파일을 업로드 하는 명령어
    - `.` : 현재 폴더 및 파일 +  하위 폴더 및 파일 모두를 의미

```bash
git add <file name>
git add .
```



- **`commit`** : 커밋 만들기
  - Staging Area에 올라온 파일들을 하나의 커밋으로 만들어주는 명령어 (스냅샷을 찍는)
  - `-m` 옵션으로 수정 이유와 같은 코멘트를 남길 수 있다.

```bash
git commit -m "commit message"
```



##### 2) 원격 관리

- **`remote add`** : 원격 저장소 등록
  - 원격 저장소 주소를 로컬에 저장하는 명령어
  - alias에는 일반적으로 `origin`

```bash
git remote add <alias> <GitHub Repository URL>

git remote -v # 등록된 원격 저장소 목록 확인
```



- **`push`** : GitHub or GitLab 과 같은 곳에 새로 생성한 커밋들 반영
  - 원격 저장소로 로컬의 커밋기록을 업로드 하는 명령어

```bash
git push <alias> <branch name> # 생성한 커밋들을 원격 저장소에 업로드
```





