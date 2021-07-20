# python_indexing



### 거꾸로 출력하고자 할 때



#### 예시

```
[입력]
banana

[출력]
ananab
```



사용자로부터 입력값을 받은 것을 거꾸로 출력해야 할 때가 있다.

그럴 때에는, 인덱스를 잘 활용해야 한다.



```python
user_word = input()

for i in range(len(user_word)):
    print(user_word[-i-1], end='')
```



1. 입력받은 값의 길이만큼 반복문을 돌린다.

   `range(len())` 

2. `[-i-1]` 로 끝에서부터 인덱싱을 수행.



✨ **`[-i-1]`**  활용도가 높을 것 같다. 잘 숙지해두자!!!

