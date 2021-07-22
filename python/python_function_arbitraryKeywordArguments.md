# python | Function



### 가변 키워드 인자 (Arbitrary Keyword Arguments)



#### 실습

- URL 생성기

```python
def my_url(**kwargs):
    base_url = 'https://api.go.kr?'
    
    for key, value in kwargs.items():
        base_url += f'{key}={value}&'
        
    return base_url
```

```
print(my_url(sidoname='서울', key='asdf'))

https://api.go.kr?sidoname=서울&key=asdf&
```

