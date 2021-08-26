# Algorithm | SWEA 6485.삼성시의 버스 노선 (python)

> 본 문제의 저작권은 SW Expert 아카데미에 있습니다.
>
> [SWEA 6485.삼성시의 버스 노선 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWczm7QaACgDFAWn&categoryId=AWczm7QaACgDFAWn&categoryType=CODE&problemTitle=6485&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

</br>

#### 문제

```
삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.

그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,

Bi이하인 모든 정류장만을 다니는 버스 노선이다.

P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.
```

</br>

#### 코드

```python
# 테스트 케이스 T 입력
T = int(input())

# T만큼 반복
for tc in range(1, T+1):
    # 버스 노선 N개 입력
    N = int(input())

    # 각 노선별로 어떤 정류장을 지나는지 체크하기 위해 stop 변수 생성
    # 5001개를 만드는 이유는 0번 인덱스부터 5000번 인덱스까지로 표현하기 위함. (0번 인덱스는 의미X)
    stop = [0] * 5001

    # N만큼 반복
    for i in range(N):
        # Ai와 Bi 에 출발/도착 정류장 값을 입력
        Ai, Bi = map(int, input().split())
        # Ai부터 Bi까지 반복하며
        for j in range(Ai, Bi +1):
            # 정류장의 j번째 인덱스에 1씩 더해준다. (해당 정류장을 통과한다는 의미)
            stop[j] += 1

    # P개의 버스 정류장 입력
    P = int(input())

    # P개의 버스 정류장을 저장하는 c_list 생성
    c_list = []

    # P만큼 반복
    for i in range(P):
        # 버스정류장 번호를 temp 변수에 저장하고, c_list에 추가
        temp = int(input())
        c_list.append(temp)

    # 결과 출력
    print('#{}'.format(tc), end=' ')
    for i in c_list:
        print(stop[i], end=' ')
    print()
```

</br>

#### 풀이

전체 버스 정류장의 리스트를 생성하고, 각각의 버스 노선이 지나가는 정류장에 숫자를 1씩 더해준다. 예를 들어, 4번 정류장의 숫자가 3이면 4번 정류장을 3번 지나간다는 의미로 해석할 수 있다. **문제를 해결하기 위한 방법을 생각하는 것이 어렵고**, 코드의 구현은 `for문` 으로 쉽게 할 수 있다.
