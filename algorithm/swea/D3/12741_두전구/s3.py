import sys
sys.stdin = open('input.txt')

T = int(input())
result = []
for _ in range(T):
    a, b, c, d = map(int, input().split())
    start = max(a, c)
    end = min(b, d)
    result.append(max(0, end - start))

for test_case in range(1, T + 1):
    print('#{} {}'.format(test_case, result[test_case - 1]))