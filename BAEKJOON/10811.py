import sys

N, M = map(int, sys.stdin.readline().split())
basket = [i + 1 for i in range(N)]

for _ in range(M):
  i, j = map(int, sys.stdin.readline().split())
  tempBasket = [basket[k-1] for k in range(i, j+1)]
  tempBasket.reverse()
  for t in range(len(tempBasket)):
    basket[i-1+t] = tempBasket[t]
print(*basket)
