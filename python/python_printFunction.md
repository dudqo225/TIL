# python_print() function



### 줄바꿈 없이 이어져 나오게 하고 싶을 때



#### 예시

```python
print('나는 홍길동입니다.')
print('나이는 30살 입니다.')

나는 홍길동입니다.
나이는 30살 입니다.
```



**↑ 위와 같은 문장을 한 줄로 출력하고 싶을 때가 있을 것이다.**

그럴 때, `print()` 함수에 두 번째 인자로 **`end=''`** 를 넣어주면 된다.



```python
print('나는 홍길동입니다.', end='')
print('나이는 30살 입니다.')

나는 홍길동입니다.나이는 30살 입니다.
```



**👍 일반적으로 `print()` 함수의 `end` 인자는 `\n` 가 기본값으로 설정 및 생략되어 있다.**
