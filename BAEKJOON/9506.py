import sys


def checkPerfect(n):
  L = []
  for i in range(n - 1):
    if n % (i + 1) == 0:
      L.append(i + 1)
  if sum(L) == n:
    return L
  else:
    return False


n = int(sys.stdin.readline())
while(n != -1):
  L = checkPerfect(n)
  if L == False:
    print(f"{n} is NOT perfect.")
  else:
    print(f"{n} = ", end="")
    for i in range(len(L) - 1):
      print(f"{L[i]} + ", end="")
    print(L[-1])
  n = int(sys.stdin.readline())
