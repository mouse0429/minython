N, K = map(int, input().split())
L = []
for i in range(N):
  if N % (i + 1) == 0:
    L.append(i + 1)

if K > len(L):
  print(0)
else:
  print(L[K - 1])
