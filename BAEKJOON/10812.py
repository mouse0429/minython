import sys

N, M = map(int, sys.stdin.readline().split())
basket = [i + 1 for i in range(N)]
for i in range(M):
  begin, end, mid = map(int, sys.stdin.readline().split())
  tempBasket = [basket[j] for j in range(mid - 1, end)]
  tempBasket += [basket[j] for j in range(begin - 1, mid - 1)]
  for k in range(len(tempBasket)):
    basket[begin - 1 + k] = tempBasket[k]
print(*basket)
