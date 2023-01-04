import sys
T = int(sys.stdin.readline())
for i in range(T):
  a, b = map(int, sys.stdin.readline().split(" "))
  result = pow(a, b, 10)
  if result == 0:
    print(10)
  else:
    print(result)