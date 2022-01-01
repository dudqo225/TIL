N = 10000

not_self_num = []
for i in range(1, N+1):
    x = i
    for j in str(i):
        x += int(j)
    not_self_num.append(x)
    if i not in not_self_num:
        print(i)