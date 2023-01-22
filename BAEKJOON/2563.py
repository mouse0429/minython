import sys

paper = [[False for _ in range(100)] for __ in range(100)]
N = int(input())
for i in range(N):
  x, y = map(int, sys.stdin.readline().split())
  for j in range(y, y + 10):
    for k in range(x, x + 10):
      paper[j][k] = True
print(sum(paper, []).count(True))
