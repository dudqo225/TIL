n = int(input())
numbers = list(map(int, input().split()))

student_num = [0] * 23

for number in numbers:
    student_num[number-1] += 1

print(*student_num)