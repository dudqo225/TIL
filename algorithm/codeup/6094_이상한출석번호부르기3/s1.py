n = int(input())
numbers = list(map(int, input().split()))

min_val = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] < min_val:
        min_val = numbers[i]

print(min_val)