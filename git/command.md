### command

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
  - nickname에는 일반적으로 `origin`

```bash
git remote add <nickname> <URL>
```



- **`push`** : GitHub or GitLab 과 같은 곳에 새로 생성한 커밋들 반영
  - 원격 저장소로 로컬의 커밋기록을 업로드 하는 명령어

```bash
git push <nickname> <branch name> # 생성한 커밋들을 원격 저장소에 업로드
```

