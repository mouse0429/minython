import sys

caseNum = 1
while True:
  L, P, V = map(int, sys.stdin.readline().split())
  if L == 0:
    break
  eResult = 0
  if ((V%P) >= L):
    eResult = L
  else:
    eResult = V%P

  result = L * (V//P) + eResult
  print(f'Case {caseNum}: {result}')
  caseNum+=1
