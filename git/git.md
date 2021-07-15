<img src="git.assets/1200px-Git-logo.svg.png" alt="초보자를 위한 깃(Git) 사용법 · Yoon&#39;s devlog" style="zoom:25%;" />



### Git 이란?

- **(분산) 버전 관리 시스템** - **DVCS**(**D**istributed **V**ersion **C**ontrol **S**ystem)
- 코드의 History를 관리하는 도구.
- 개발된 과정과 역사를 볼 수 있으며, 프로젝트 이전 버전을 복원하고 변경 사항을 비교, 분석 및 병합이 가능
- **차이(diff)** 가 무엇이고, 수정 이유를 log로 남길 수 있다.



***



### Git_command

- **`init`** : 로컬 저장소 설정



- **`add`** : 커밋할 목록에 추가



- **`commit`** : 커밋 만들기
  - `-m` 옵션으로 수정 이유와 같은 코멘트를 남길 수 있다.

```bash
git commit -m "add README.md"
```



- **Author(작성자) 설정**
  - `user.name` : 사용자명
  - `user.email` : 이메일 주소 (GitHub 계정과 일치)

```bash
git config --global user.name <사용자명>
git config --global user.email <이메일 주소>

git config --global -l # git 설정 확인
```



- **`remote`** : 원격 저장소 등록

```bash
git remote add origin <GitHub Repository 주소>

git remote -v # 등록된 원격 저장소 목록 확인
```



- **`origin`** : 



- **`push`** : GitHub or GitLab 과 같은 곳에 새로 생성한 커밋들 반영

```bash
git push origin master # 생성한 커밋들을 원격 저장소에 업로드
```





