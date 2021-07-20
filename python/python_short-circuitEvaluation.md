# python | short-circuit evaluation (단축평가)



### short-circuit evaluation (단축평가) 란?

- 첫 번째 값이 확실할 때, 두 번째 값은 확인하지 않는 것
- 뒷 부분의 판단이 필요없기 때문에 속도가 향상됨



##### 1. and 는 a가 거짓이면 a를 리턴. 참이면 b를 리턴

```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)

True
False
False
False
-----------------------------
print(3 and 5)
print(3 and 0)
print(0 and 3)
print(0 and 0)

5
0
0
0
```



##### 2. or 는 a가 참이면 a를 리턴. 거짓이면 b를 리턴

```python
print(True or True)
print(True or False)
print(False or True)
print(False or False)

True
True
True
False
-----------------------------
print(3 or 5)
print(3 or 0)
print(0 or 3)
print(0 or 0)

3
3
3
0
```

