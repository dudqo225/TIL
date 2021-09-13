# Algorithm | SWEA 4880.토너먼트 카드게임 (python)

> 본 문제의 저작권은 SW Expert 아카데미에 있습니다.
>
> [SWEA 4880.토너먼트 카드게임 링크](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

</br>

#### 문제

```
사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다. 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다. 게임 룰은 다음과 같다.

1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.

그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 두개로 나눈다.

두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다.

다음은 4명이 카드를 비교하는 경우로, 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다. 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는 바꾸지 않는다.

N명이 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만드시오.
```

<br>

#### 코드

```python
# 가위바위보 게임
def RPS(left, right):
    l, r = cards[left-1], cards[right-1]

    # 같을 경우, 인덱스가 낮은 사람이 이긴다.
    if l == r:
        return left
    # 가위
    elif l == 1:
        if r == 3:
            return left
        elif r == 2:
            return right
    # 바위
    elif l == 2:
        if r == 1:
            return left
        elif r == 3:
            return right
    # 보
    elif l == 3:
        if r == 1:
            return right
        elif r == 2:
            return left

# card game 함수
def cardGame(low, high):
    if low == high:
        return low
    else:
        # 중간 인덱스 설정
        mid = (low + high) // 2

        l = cardGame(low, mid)
        r = cardGame(mid+1, high)
        return RPS(l, r)

# 테스트 케이스 T 입력
T = int(input())
for tc in range(1, T+1):
    # 인원수 N 입력
    N = int(input())
	
    # N개의 카드 리스트 입력
    cards = list(map(int, input().split()))
	
    # 결과값 ans
    ans = cardGame(1, N)
	
    # 결과 출력
    print('#{} {}'.format(tc, ans))
```

<br>

#### 풀이

 문제를 굉장히 오랜만에 다시 봐서, 전혀 모르겠다. 다른 사람들이 푼 코드를 참고하여 **재귀** 형식으로 코드를 구현하였는데 잘 이해가 되지 않는다.

 코드는 가위바위보 게임에서 이긴 사람을 찾는 함수 `RPS` 와 좌-우 사람이 게임을 진행해서 승자를 찾는 `cardGame` 함수로 이루어져 있다. 특히, `cardGame` 함수 내부에서 재귀 호출이 이루어지는데, 다른 사람 코드를 보면 이 부부분의 `l` , `r` 을 **Divide and Conquer** 방식으로 푼 케이스도 있었다. 근데 코드 자체는 매우 비슷했다.

<br>

#### 결론

 이 문제는 내가 푼 문제가 아니다. 다른 사람한테 다시 물어보고 처음부터 다시 풀어봐야겠다. 2021.09.13
