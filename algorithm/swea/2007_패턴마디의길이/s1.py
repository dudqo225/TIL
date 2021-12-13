import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = input()

    Q = [words[0]]
    i = 1

    while True:
        if Q[0] == words[i]:
            if Q[1] == words[i+1]:
                break
            else:
                Q.append(words[i])
                i += 1
        else:
            Q.append(words[i])
            i += 1

    ans = len(Q)

    print('#{} {}'.format(tc, ans))