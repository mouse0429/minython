import sys

def recursion(s, l, r, n):
  if l >= r:
    return 1, n
  elif s[l] != s[r]:
    return 0, n
  else:
    return recursion(s, l + 1, r - 1, n + 1)

T = int(sys.stdin.readline())
for i in range(T):
  S = sys.stdin.readline().strip()
  print(*recursion(S, 0, len(S) - 1, 1))
