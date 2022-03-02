# Algorithm | 백준 9241.바이러스 복제 (python)

> 본 문제의 저작권은 BAEKJOON에 있습니다.
>
> [백준 9241.바이러스 복제 링크](https://www.acmicpc.net/problem/9241)

</br>

#### 문제

상근이는 DNA의 일부를 교체해 복제를 시작하는 바이러스를 발견했다.

이 바이러스는 어떤 DNA의 연속된 일부분을 다른 DNA로 교체한다.

이제, 다음 연구를 위해 바이러스에 의해 교체된 DNA의 길이를 구해보려고 한다.

바이러스에 감염되기 전 DNA와 감염된 후 DNA가 주어진다. 두 번째 DNA로 바뀌기 위해 첫 번째 DNA에 삽입되어야 하는 연속된 DNA 조각의 길이를 구하는 프로그램을 작성하시오.

연속된 DNA 조각은 삽입되기 전, 원래 그 자리에 있는 DNA를 제거할 수도 있다.

</br>

#### 입력

첫째 줄에 바이러스에 감염되기 전 DNA, 둘째 줄에 감염된 후의 DNA가 주어진다.

DNA는 {A, G, C, T}로만 이루어져 있으며, 길이는 1보다 크거나 같고, 105보다 작거나 같다.

</br>

#### 출력

첫째 줄에 바이러스에 의해 삽입된 DNA 길이의 최솟값을 출력한다.

</br>

#### 코드

```python
origin_dna = input()
infected_dna = input()

checked = [0] * min(len(origin_dna), len(infected_dna))

# 접두사 체크
for i in range(len(checked)):
    if origin_dna[i] == infected_dna[i]:
        checked[i] = 1
    else:
        break

# 접미사 체크
for i in range(len(checked)):
    if origin_dna[len(origin_dna) - i - 1] == infected_dna[len(infected_dna) - i -1]:
        checked[len(checked) - i - 1] = 1
    else:
        break

# 일치하는 DNA 개수 카운트
used_word_cnt = 0
for i in range(len(checked)):
    if checked[i]:
        used_word_cnt += 1

print(max(len(infected_dna) - used_word_cnt, 0))
```

</br>

#### 풀이

- `감염 전 DNA`와 `감염 후 DNA` 를 비교하는데,
- 각 자리의 DNA를 비교해서 일치하는지 여부를 확인하는 `checked` 변수를 선언하고 앞에서 부터 비교(접두사) 하는 방법 + 뒤에서 부터 비교(접미사) 하는 방법 **2가지** 반복문을 수행해야 한다.
- 두 번의 반복문이 종료되면 `checked` 변수를 순회하면서 일치하는 DNA의 숫자를 카운트해준다. `감염된 DNA의 길이 - 일치하는 DNA 개수` 와 `0` 중에서 최대값을 결과값으로 출력한다.
  - `감염된 DNA의 길이 - 일치하는 DNA 개수` 의 결과값이 음수가 나올 수 있는데, 이와 같은 CASE의 답은 `0` 으로 출력하기 위함이다.
