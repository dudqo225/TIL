w, h, b = map(int, input().split())

ans = w * h * b / 8 / 1024 / 1024

print('{:.2F} MB'.format(ans))
