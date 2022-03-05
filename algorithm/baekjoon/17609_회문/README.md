# Algorithm | 백준 17609.회문 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 17609.회문 링크](https://www.acmicpc.net/problem/17609)

</br>

#### 문제

회문(回文) 또는 팰린드롬(palindrome)은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열을 말한다. 예를 들어 ‘abba’ ‘kayak’, ‘reviver’, ‘madam’은 모두 회문이다. 만일 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열을 “유사회문”(pseudo palindrome)이라고 부른다. 예를 들어 ‘summuus’는 5번째나 혹은 6번째 문자 ‘u’를 제거하여 ‘summus’인 회문이 되므로 유사회문이다.

여러분은 제시된 문자열을 분석하여 그것이 그 자체로 회문인지, 또는 한 문자를 삭제하면 회문이 되는 “유사회문”인지, 아니면 회문이나 유사회문도 아닌 일반 문자열인지를 판단해야 한다. 만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다. 

</br>

#### 입력

입력의 첫 줄에는 주어지는 문자열의 개수를 나타내는 정수 T(1 ≤ T ≤ 30)가 주어진다. 다음 줄부터 T개의 줄에 걸쳐 한 줄에 하나의 문자열이 입력으로 주어진다. 주어지는 문자열의 길이는 3 이상 100,000 이하이고, 영문 알파벳 소문자로만 이루어져 있다.

</br>

#### 출력

각 문자열이 회문인지, 유사 회문인지, 둘 모두 해당되지 않는지를 판단하여 회문이면 0, 유사 회문이면 1, 둘 모두 아니면 2를 순서대로 한 줄에 하나씩 출력한다.

</br>

#### 코드

##### s1

```python
def palilndrome_check(checking_words):
    if checking_words == checking_words[::-1]:
        return 0

    for i in range(len(checking_words)):
        copy_words = checking_words[:]
        del copy_words[i]
        if copy_words == copy_words[::-1]:
            return 1

    return 2

T = int(input())
for tc in range(1, T+1):
    words = list(sys.stdin.readline().rstrip())
    ans = palilndrome_check(words)
    print(ans)
```

- **시간 초과**
- 처음 `if` 문은 회문인지 여부를 조사하는 코드로, `[::-1]` 를 활용하여 주어진 문자열을 뒤집어서 비교한다.
- 다음 `for` 문은 유사회문 여부를 체크하는 코드로, 주어진 문자열을 복사하고 (`copy_words`) `i` 번째 문자를 지운 후 회문 여부를 조사한다. 이 부분 때문에 시간초과가 뜬 것 같다. 문제 조건을 보면 문자열의 길이가 최대 100,000 이기 때문에 시간복잡도가 커지기 때문에 다른 방식으로 문제를 해결해야 했다.

</br>

##### s2

```python
def pseudo_check(check_words, start, end):
    while start < end:
        if check_words[start] == check_words[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


def palindrome_check(check_words, start, end):
    while start < end:
        if check_words[start] == check_words[end]:
            start += 1
            end -= 1
        else:
            pseudo1 = pseudo_check(check_words, start+1, end)
            pseudo2 = pseudo_check(check_words, start, end-1)

            if pseudo1 or pseudo2:
                return 1
            else:
                return 2
    return 0


T = int(input())
for _ in range(T):
    words = sys.stdin.readline().rstrip()
    ans = palindrome_check(words, 0, len(words)-1)
    print(ans)
```

</br>

#### 풀이

- 주어진 문자열과 시작 인덱스, 끝 인덱스를 사용하는 함수를 작성하였다.
- 앞/뒤 문자를 비교하면서 같은 문자라면 `start`는 `1` 씩 증가하고, `end` 는 `1` 씩 감소한다. `while` 문이 정상적으로 종료되면 회문이기 때문에 `1` 을 반환한다.
- 만약 비교하는 문자가 다르다면, 유사 회문 여부를 체크하는 `pseudo_check` 함수를 시행한다. 이때, 시작 문자를 제거하거나 / 끝 문자를 제거하거나 **2가지**로 나누어서 함수를 2번 시행한다. 이 함수에서도 마찬가지로 앞/뒤 문자를 비교하는데 한 번이라도 문자가 다르다면 유사회문이 될 수 없기 때문에 `False` 를 반환하고, 정상적으로 `while` 문이 종료되면 유사회문이므로 `True`를 반환한다.
- `pseudo1` 과 `pseudo2` 둘 중 하나의 값이  `True` 라면 유사회문이므로 `1`을 반환하고, 아니라면 `2`를 반환한다.
