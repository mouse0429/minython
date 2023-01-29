N = int(input())

for i in range(N):
  print(" "*(N-1-i), end="")
  print("*"*(2*i+1))

for i in range(N-1, 0, -1):
  print(" "*(N-i), end="")
  print("*"*(2*i-1))