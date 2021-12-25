import sys
sys.stdin = open('input.txt')

N = int(input())

members = []

for i in range(N):
    age, name = input().split()
    members.append([int(age), name, i])

members = sorted(members, key= lambda x : (x[0], x[2]))

for member in members:
    print('{} {}'.format(member[0], member[1]))