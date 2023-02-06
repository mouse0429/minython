def checkP(S):
  L = len(S)
  for i in range(L // 2):
    if S[i] == S[L - 1 - i]:
      continue
    else:
      return 0
  return 1

S = input()
print(checkP(S))