inputL = [int(input()) for _ in range(5)]
inputL.sort()
print(sum(inputL) // 5)  # mean
print(inputL[2])  # median