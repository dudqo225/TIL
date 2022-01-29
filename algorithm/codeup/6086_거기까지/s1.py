n = int(input())

total = 0
i = 1
while True:
    total += i
    i += 1

    if total >= n:
        break

print(total)