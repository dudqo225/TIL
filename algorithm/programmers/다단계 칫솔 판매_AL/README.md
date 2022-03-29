# Programmers | 다단계 칫솔 판매 (AL)

> 본 문제의 저작권은 프로그래머스에 있습니다.
>
> [다단계 칫솔 판매 링크](https://programmers.co.kr/learn/courses/30/lessons/77486)

</br>

#### 문제 설명 및 제한사항

문제가 너무 길다... [링크](https://programmers.co.kr/learn/courses/30/lessons/77486)를 참고하자

</br>

#### 코드

- **solution.py**
  - `cost`를 0.9 또는 0.1로 나누면 오차가 발생할 수 있다.
  - 또한, `.index()` 메소드 사용으로 인해 **시간초과**가 발생할 수 있다.

```python
def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)

    def find_ref(seller_name, cost):
        ref_i = enroll.index(seller_name)
        ref = referral[ref_i]

        if ref == "-":
            answer[ref_i] += round(cost * 0.9)
            return

        if cost * 0.1 < 1:
            answer[ref_i] += cost
        else:
            answer[ref_i] += round(cost * 0.9)
            find_ref(ref, round(cost * 0.1))

        return

    for i in range(len(seller)):
        benefit = amount[i] * 100
        find_ref(seller[i], benefit)

    return answer
```

</br>

- **solution2.py**

```python
def solution(enroll, referral, seller, amount):
    answer = []
    
    rev = dict()
    parent = dict()
    for i in range(len(enroll)):
        rev[enroll[i]] = 0
        parent[enroll[i]] = referral[i]
        
    def find_ref(seller_name, cost):
        ref = parent[seller_name]

        if ref == "-":
            rev[seller_name] += (cost - cost // 10)
            return

        if cost * 0.1 < 1:
            rev[seller_name] += cost
        else:
            rev[seller_name] += (cost - cost // 10)
            find_ref(ref, cost // 10)

        return

    for i in range(len(seller)):
        benefit = amount[i] * 100
        find_ref(seller[i], benefit)
        
    for r in rev:
        answer.append(rev[r])

    return answer
```

</br>

#### 풀이

- 각 판매원을 다단계 조직에 참여시킨 판매원을 **key-value** 형태로 `parent` 딕셔너리에 저장한다.
- `rev` 딕셔너리는 각 판매원의 수익을 저장하는 딕셔너리이다. **value**는 `0`으로 초기화한다.
- `find_ref` 함수를 통해서 각 판매원의 수익과 판매원을 조직에 가입시킨 판매원의 수익을 **재귀적**으로 계산해 나아간다.
  - **10%** 수익과 **90%** 수익은 0.1, 0.9을 곱해서 계산하지 않는다 (오차가 발생하기 때문)
  - **10%** 수익 - `cost // 10`
  - **90%** 수익 - `cost - cost // 10`

- 함수 종료 이후에 `rev` 딕셔너리를 순회하면서 각 key 값의 value 값을 `answer` 리스트에 추가한다.