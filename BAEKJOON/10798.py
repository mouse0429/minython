arr = [[""] * 15 for _ in range(5)]

for i in range(5):
  s = input()
  for j in range(len(s)):
    arr[i][j] = s[j]

for i in range(15):
  for j in range(5):
    print(arr[j][i], end="")
