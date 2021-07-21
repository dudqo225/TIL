# python | Error & Exception Handling 에러 및 예외 처리



### Error

- 문법 에러 (Syntax Error)

  - 줄에서 에러가 감지된 가장 앞 위치를 `^` 캐럿 기호로 표시

- 종류

  - Invalid syntax : 구문 자체에 오류가 있음
  - assign to literal : 리터럴에 할당을 하려 할 때 발생

  ```
  5 = 3
  SyntaxError 발생
  ```

  - EOL (End of Line) : 한 줄 코드가 마무리 되지 않았을 때
  - EOF (End of File) : 파일의 끝이 마무리 되지 않았을 때



### Exception

- Syntax Error 이외의 에러 - 문법적으로 올바르더라도 발생하는 에러를 일컬음

- 실행 중 감지되는 에러

- 내장 예외는 Exception Class를 상속

- 사용자 정의 예외를 만들고 관리 가능

- 종류

  - ZeroDivisionError :  `0` 으로 나누려 할 때 발생

  - NameError : namespace 상에 이름이 없는 경우 발생

  - TypeError

    - 타입 불일치

    ```python
    1 + '1'
    int + str 은 성립 불가능
    ```

    - argument 누락

    ```python
    divmod()
    () 괄호 안에 2개의 인자가 있어야 함
    ```

    - argument 갯수 초과

    ```python
    divmod(1, 2, 3)
    () 괄호 안에 2개의 인자가 가능하나, 3개 인자가 들어옴
    ```

    - argument type 불일치

  - ValueError : 타입은 올바르지만 값이 적절하지 않은 경우

  - IndexError : 인덱스가 존재하지 않거나 or 범위를 벗어난 경우

  - KeyError : 해당 키가 존재하지 않는 경우

- **Exception 종류는 많이 있으며, 굳이 외울 필요는 X**

- 파이썬 내장 예외 (built-in-exceptions)

  [파이썬 공식 문서 - 내장 예외](https://docs.python.org/ko/3/library/exceptions.html)

  

### Exception Handling

- **try** 문 / **except** 절을 이용하여 예외 처리 가능

```python
try:
    user_input = input('숫자를 입력하세요: ')
    print(int(num))
except ValueError:
    print('숫자가 입력되지 않았습니다.')
    
숫자를 입력하세요: 안녕하세요
숫자가 입력되지 않았습니다.
```

- 복수의 예외 처리도 가능

```python
try:
    user_input = input('100으로 나눌 값을 입력하세요: ')
    100 / int(user_input)
except (ValueError, ZeroDivisonError): #괄호() 안에 콤마, 로 구분
    print('다시 입력하세요!')
```

```python
try:
    user_input = input('100으로 나눌 값을 입력하세요: ')
    100 / int(user_input)
except ValueError: # 첫 번째 예외 처리
    print('숫자를 입력해주세요.')
except ZeroDivisonError: # 두 번째 예외 처리
    print('0으로 나눌 수 없습니다.')
except: # 마지막 예외 처리
    print('오류가 발생하였습니다. 다시 입력해주세요.')
```

- **복수 예외 처리는 순차적으로 수행되기 때문에, 가장 작은 범주부터 예외 처리 해주어야 한다.**

- `try` : 코드를 실행
- `except` : try 문에서 예외 발생시 실행
- `else` : try 문에서 예외가 발생하지 않으면 실행
- `finally` : 예외 발생 여부와 관계없이 항상 실행



### 예외 발생 시키기

- `raise` 를 통해 예외를 강제로 발생 시킬 수 있다.
- `assert` 를 통해 예외를 강제로 발생 → 무조건 **AssertionError** 가 발생
- **디버깅 용도로 사용**



#### EAFP vs LBYL

- **EAFP** : Easier to ask for forgiveness than permission
  - *허락보다는 용서 구하기가 쉽다.*
  - `try` - `except` 구문의 특징
  - 가정이 옳다고 전제하고, 가정이 틀리면 예외를 잡는다
- **LBYL** :  Look before you leap
  - *뛰기 전에 보라*
  - `if` 문의 특징
  - 명시적으로 사전 조건들을 검사















