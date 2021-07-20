# python | nested loop (중첩 반복문)



### 중첩 루프란?

- 반복문 여러개가 겹쳐져 있는 구조



#### 예시

- 계단 만들기

```python
N = int(input())

for i in range(1, N+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

[입력]
5

[출력]
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
```



**✨중첩 구조는 반복문, 조건문 등에서 자주 활용된다. 친숙해지자!**

