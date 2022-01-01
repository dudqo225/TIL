def func1(h):
    global time
    result = 0

    for i in list_a:
        if result> time:
            return 100000000000000,0
        if h>i:
            result+=(h-i)
        elif h < i:
            result+=(i-h)*2
    return result,h

N, M, B = map(int,input().split())
list_a=[]
for _ in range(N):
    list_a+=map(int,input().split())

time=10000000000000
height=0
for h in range(min(list_a), max(list_a)+1):
    if sum(list_a)+B >= h*N*M:
        a,b = func1(h)
    if time>=a:
        time=a
        height = b

print(time, height)