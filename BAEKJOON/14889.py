from itertools import combinations
import sys

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

L = list(combinations([i + 1 for i in range(N)], N // 2))

answer = -1

for i in range(len(L) // 2):
  start, link = 0, 0
  for ij in list(combinations(list(L[i]), 2)):
    start += S[ij[0]-1][ij[1]-1] + S[ij[1]-1][ij[0]-1]
  for ij in list(combinations(list(L[len(L) - 1 - i]), 2)):
    link += S[ij[0]-1][ij[1]-1] + S[ij[1]-1][ij[0]-1]
  if answer == -1 or answer > abs(start - link):
    answer = abs(start - link)

print(answer)
