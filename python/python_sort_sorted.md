# python | .sort() vs sorted()



### .sort()

- 원본 데이터 자체를 수정

```python
number1 = [1, 2, 3, 7, 4, 2, 2, 1]

number1.sort()

print(number1)
[1, 1, 2, 2, 2, 3, 4, 7]
```



### sorted()

- 원본 데이터를 그대로 두고 새롭게 정렬한 값을 반환

```python
number1 = [1, 2, 3, 7, 4, 2, 2, 1]

print(sorted(number1))
[1, 1, 2, 2, 2, 3, 4, 7]

print(number1)
[1, 2, 3, 7, 4, 2, 2, 1]
```



**✨ .sort() 와 sorted() 가 용어 자체가 비슷하다 보니, 헷갈린다. 주의하자!**

