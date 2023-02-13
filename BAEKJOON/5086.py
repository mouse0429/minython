import sys

N, M = map(int, sys.stdin.readline().split())
while N != 0 or M != 0:
  if N < M:
    if M % N == 0:
      print("factor")
    else:
      print("neither")
  else:
    if N % M == 0:
      print("multiple")
    else:
      print("neither")
  N, M = map(int, sys.stdin.readline().split())