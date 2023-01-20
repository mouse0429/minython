row = 1
col = 1
max = 0
table = [list(map(int,input().split())) for _ in range(9)]

for i in range(9):
  for j in range(9):
    if max < table[i][j]:
      row = i+1
      col = j+1
      max = table[i][j]

print(max)
print(row, col)