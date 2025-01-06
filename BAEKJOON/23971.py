H, W, N, M = map(int, input().split())

row = W // (M+1)
if W % (M+1) != 0:
    row += 1
col = H // (N+1)
if H % (N+1) != 0:
    col += 1

print(col*row)
