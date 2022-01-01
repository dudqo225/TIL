import sys
sys.stdin = open('input.txt')

import itertools

dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

dwarfs.sort()

dwarfs_combinations = list(itertools.combinations(dwarfs, 7))

for dwarfs_combination in dwarfs_combinations:
    if sum(dwarfs_combination) == 100:
        for dwarf in dwarfs_combination:
            print(dwarf)
        break