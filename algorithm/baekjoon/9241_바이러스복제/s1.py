import sys
sys.stdin = open('input.txt')

origin_dna = input()
infected_dna = input()

origin_dna_length = len(origin_dna)
infected_dna_length = len(infected_dna)

checked = [0] * min(origin_dna_length, infected_dna_length)

for i in range()