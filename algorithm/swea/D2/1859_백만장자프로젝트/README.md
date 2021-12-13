# Algorithm | SWEA 1859.백만장자 프로젝트 (python)

> 본 문제의 저작권은 SW Expert 아카데미에 있습니다.
>
> [SWEA 1859.백만장자 프로젝트 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=1859&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

</br>

#### 문제

```
25년 간의 수행 끝에 원재는 미래를 보는 능력을 갖게 되었다. 이 능력으로 원재는 사재기를 하려고 한다. 다만 당국의 감시가 심해 한 번에 많은 양을 사재기 할 수 없다.
다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.

1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
3. 판매는 얼마든지 할 수 있다.

예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.
```

</br>

#### 코드

```python
# 테스트 케이스 개수 T 입력
T = int(input())

# T만큼 반복
for tc in range(1, T+1):
    # 자연수 N의 개수 입력
    N = int(input())
    # N 리스트 입력
    N_list = list(map(int, input().split()))

    # N_list의 마지막 값을 최대값으로 설정
    max_value = N_list[-1]
    # 이익 변수 초기화
    profit = 0

    # N-2번째 인덱스부터 0번째 인덱스까지 1씩 감소하면서 반복 순회
    for i in range(N-2, -1, -1):
        # 만약 현재 매매가가 최대값보다 크면 최대값을 변경
        if N_list[i] >= max_value:
            max_value = N_list[i]
        # 현재 매매가가 최대값보다 크지 않으면 차익을 profit 변수에 더해준다
        else:
            profit += max_value - N_list[i]
    
    # 결과 출력
    print('#{} {}'.format(tc, profit))
```

</br>

#### 풀이

**거꾸로 계산하기** <br>**마지막날 매매가를 최대값으로 설정**한다. 하루씩 앞으로 **날짜를 거슬러 오면서 그 날의 매매가와 비교**를 하는데, 만약 i번째 날의 매매가가 현재 최대값보다 크면 최대값을 i번째 날 매매가로 변경해준다. 반대로 i번째 날의 매매가가 현재 최대값보다 크지 않다면 최대값과 i번째 날 매매가의 차이 즉, 이익을 계산해서 총이익에 더해준다.

