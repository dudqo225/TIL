import sys
sys.stdin = open('input.txt')

'''
sys.stdin.readline() 으로 input()을 대체하고,
sys.stdout.write() 로 print()를 대체하여,
입/출력 시간을 줄여서 문제를 해결한다.
'''


N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

for i in sorted(num_list):
    sys.stdout.write(str(i)+'\n')