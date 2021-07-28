# python | Module 모듈



## 모듈과 패키지

- **모듈**
  - 특정 기능을 파이썬 파일(.py) 단위로 작성한 것
- **패키지**
  - 특정 기능과 관련된 여러 모듈의 집합
  - 패키지 안에는 또 다른 서브 패키지를 포함한다

### 모듈

- 파이썬 표준 라이브러리(Python Standard Library, PSL)

  - 파이썬에 기본적으로 설치된 모듈과 내장 함수
  - [파이썬 표준 라이브러리 링크](https://docs.python.org/ko/3/library/index.html)
  - 예시 - random.py

- 파이썬 패키지 관리자(pip)

  - PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

  - pip 명령어

    - 패키지 설치

      - 최신 / 특정 / 최소 버전을 명시하여 설치할 수 있음
      - 이미 설치되어 있는 경우 "이미 설치되어 있음"을 알리고 아무것도 하지 않음

      ```bash
      $ pip install <package name>
      $ pip install <package name>==1.0.5
      $ pip install <package name>>=1.0.4
      ```

    - 패키지 삭제

      - 패키지를 업그레이드하는 경우 과거 버전을 자동으로 지워줌

      ```bsah
      $ pip uninstall <package name>
      ```

    - 패키지 목록 및 특정 패키지 정보

      ```bash
      $ pip list
      $ pip show <package name>
      ```

    - 패키지 `freeze`

      - 설치된 패키지들의 목록을 만들고, `pip install` 에서 활용되는 형식으로 출력
      - 해당 목록을 requirements.txt 로 만들어 관리함 (관습)

      ```bash
      $ pip freeze > requirements.txt
      $ pip install -r requirements.txt # requirements.txt를 바탕으로 패키지를 설치
      ```



### 가상환경

- PSL이 아닌 외부 패키지/모듈을 사용하는 경우 모두 pip를 통해 설치해야 함
- 여러개의 프로젝트를 진행하는 경우 버전이 서로 다를 수 있다
  - 과거 외주 PJT - django 버전 2.x
  - 신규 회사 PJT - django 버전 3.x
- 이럴 경우 가상환경을 만들어 PJT 별로 독립적인 패키지를 관리할 수 있다

#### venv

- 가상 환경을 만들고 관리하는데 사용하는 모듈 (Python 3.5 버전부터)

- 특정 디렉토리에 가상 환경을 만들고, 고유한 패키지 집합을 가질 수 있다

  - 특정 폴더에 가상 환경(패키지 집합 폴더 등)이 구성되어 있고
  - `bash` 와 같은 실행환경에서 가상환경을 활성화 시켜서
  - 해당 폴더에 있는 패키지를 관리하고 사용

- 가상환경 생성

  - 해당 디렉토리에 별도의 파이썬 패키지가 설치됨

  ```bash
  $ python -m venv <folder name> # folder name은 일반적으로 venv
  ```

- 가상환경 활성화/비활성화

  - 명령어를 통해 가상환경을 활성화/비활성화

  ```bash
  $ source venv/Scripts/activate # 활성화
  $ deactivate # 비활성화
  ```



### 모듈/패키지 활용하기

- 패키지

  - 패키지는 여러 모듈/하위 패키지로 구조화 되어 있다

    - 예시 : `package.module`

  - 모든 폴더에는 `__init__.py` 를 만들어 패키지로 인식

    - Python 3.3부터는 위 파일이 없어도 된다. But, 하위 버전 호환 및 프레임워크 등에서의 원활한 동작을 위해 파일 생성할 것을 권장함

  - 예시

    - 폴더 구조

    ```
    my_package/
        __init__.py
        math/
            __init__.py
            tools.py
        statistics/
            __init__.py
            tools.py
    
    # 패키지는 총 3개 - my_package, math, statistics
    # 모듈은 총 2개 - math/tools, statistics/tools
    # __init__.py는 패키지임을 명시해주는 파일. 파일 내에는 아무런 내용도 작성하지 않음
    ```

- 다양한 모듈 사용법

```
> import module
> from module import var, function, Class
> from module import *

> from package import module
> from package.module import var, function, Class
```

