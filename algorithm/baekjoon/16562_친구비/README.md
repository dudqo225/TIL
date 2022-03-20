# Algorithm | 백준 16562.친구비 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 16562.친구비 링크](https://www.acmicpc.net/problem/16562)

</br>

#### 문제

19학번 이준석은 학생이 N명인 학교에 입학을 했다. 준석이는 입학을 맞아 모든 학생과 친구가 되고 싶어한다. 하지만 준석이는 평생 컴퓨터랑만 대화를 하며 살아왔기 때문에 사람과 말을 하는 법을 모른다. 그런 준석이에게도 희망이 있다. 바로 친구비다!

학생 i에게 *Ai*만큼의 돈을 주면 그 학생은 1달간 친구가 되어준다! 준석이에게는 총 k원의 돈이 있고 그 돈을 이용해서 친구를 사귀기로 했다. 막상 친구를 사귀다 보면 돈이 부족해질 것 같다는 생각을 하게 되었다. 그래서 준석이는 “친구의 친구는 친구다”를 이용하기로 했다.

준석이는 이제 모든 친구에게 돈을 주지 않아도 된다!

위와 같은 논리를 사용했을 때, 가장 적은 비용으로 모든 사람과 친구가 되는 방법을 구하라.

</br>

#### 입력

첫 줄에 학생 수 N (1 ≤ N ≤ 10,000)과 친구관계 수 M (0 ≤ M ≤ 10,000), 가지고 있는 돈 k (1 ≤ k ≤ 10,000,000)가 주어진다.

두번째 줄에 N개의 각각의 학생이 원하는 친구비 *Ai*가 주어진다. (1 ≤ *Ai* ≤ 10,000, 1 ≤ i ≤ N)

다음 M개의 줄에는 숫자 v, w가 주어진다. 이것은 학생 v와 학생 w가 서로 친구라는 뜻이다.

</br>

#### 출력

준석이가 모든 학생을 친구로 만들 수 있다면, 친구로 만드는데 드는 최소비용을 출력한다. 만약 친구를 다 사귈 수 없다면, “`Oh no`”(따옴표 제거)를 출력한다.

</br>

#### 코드

```python
import sys

# 재귀 limit 변경
sys.setrecursionlimit(10 ** 9)


# 입력받은 값 x와 친구인 친구들 목록을 반환하는 함수
def check(x, friends_list):
    global arr, visited, ans

    visited[x] = 1

    for i in arr[x]:
        if not visited[i]:
            friends_list.append(i)
            check(i, friends_list)

    return friends_list


N, M, k = map(int, input().split())

costs = [0] + list(map(int, input().split()))

# 인접 리스트
arr = [[] for _ in range(N+1)]
for _ in range(M):
    v, w = map(int, input().split())
    # 양방향
    arr[v].append(w)
    arr[w].append(v)

visited = [0] * (N+1)
ans = []

# 1부터 N까지 순회
for i in range(1, N+1):
    if not visited[i]:
        # check 함수를 통해 친구들 목록 생성
        friends = check(i, [i])

        min_cost = 9876543210

        # 친구들을 한명씩 확인하면서 친구비가 가장 작은 값을 찾아서 ans에 추가
        for friend in friends:
            if min_cost > costs[friend]:
                min_cost = costs[friend]
        ans.append(min_cost)

# ans의 총합이 k보다 작으면 ans 총합 출력
if sum(ans) <= k:
    print(sum(ans))

# 총합이 k보다 크면 Oh ho 출력
else:
    print("Oh no")
```

</br>

#### 풀이

- **그래프** 문제
- 인접 리스트를 생성하고, `v`번째 리스트에 `w`를 추가해준다.
- `check(x, friends_list)` 함수는 입력받은 값 `x`와 친구인 친구들의 목록을 반환하는 함수이다.
- `1` 부터 `N` 까지 반복하면서 친구 목록을 생성하고, 친구들 중에서 **친구비**가 가장 작은 값을 `ans` 리스트에 추가한다.
- 반복문이 종료되고 나면, `ans`의 총합을 계산하고 `k` 보다 작거나 같으면 총합을, 크면 **"Oh no"** 를 출력한다.
- 파이썬의 최대 재귀 깊이는 1000이므로, `sys.setrecursionlimit()` 를 통해서 최대 재귀 깊이를 늘려준다.

</br>

구글링을 해보니, **Union-Find** 로 문제를 푼 사람들이 훨씬 많았다. 재귀 깊이를 바꾸지 않고, 일반적으로 풀려면 이 방식이 맞는 것 같다. 분명히 1학기 때 배웠는데 왜 기억이 안나지..ㅎㅎㅎ

https://jjangsungwon.tistory.com/122
