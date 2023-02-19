import sys

def merge(A,p,q,r):
  temp = [A[i] for i in range(p,r+1)]
  temp.sort()
  for j in range(len(temp)):
    global K
    if K == 1:
      print(temp[j])
    K -=1

def merge_sort(A, p, r):
  if p < r:
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
answer = merge_sort(A, 0, N - 1)
if K >= 1:
  print(-1)
