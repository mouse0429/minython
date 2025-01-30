positions = [list(map(int, input().split())) for _ in range(3)]
positions.sort(key=lambda x: x[0])

if (positions[2][0] - positions[1][0] == 0 and positions[1][0] - positions[0][0] == 0):
    print("WHERE IS MY CHICKEN?")
elif (positions[2][0] - positions[1][0] == 0 or positions[1][0] - positions[0][0] == 0):
    print("WINNER WINNER CHICKEN DINNER!")
elif (positions[2][1] - positions[1][1]) / (positions[2][0] - positions[1][0]) == (positions[1][1] - positions[0][1]) / (positions[1][0] - positions[0][0]):
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")
