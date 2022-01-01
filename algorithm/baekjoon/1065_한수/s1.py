import sys
sys.stdin = open('input.txt')

def check(X):
    if X < 100:
        return True
    else:
        X = str(X)
        diff_1 = int(X[1]) - int(X[0])
        for i in range(2, len(X)):
            diff_2 = int(X[i]) - int(X[i-1])
            if diff_1 != diff_2:
                return False
        return True

N = int(input())

ans = 0
for i in range(1, N+1):
    if check(i):
        ans += 1

print(ans)