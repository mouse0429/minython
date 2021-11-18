import sys
from itertools import combinations
N, K = map(int, sys.stdin.readline().split())
Nlist = [0]*N

print(len(list(combinations(Nlist,K))))