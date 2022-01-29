n = int(input())
numbers = list(map(int, input().split()))

print(*numbers[::-1])