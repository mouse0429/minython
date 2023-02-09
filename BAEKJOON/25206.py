import sys

gradeToScore = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
                "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
totalScore = 0
totalMul = 0

for i in range(20):
  _, mul, grade = sys.stdin.readline().split()
  if grade == "P":
    continue
  else:
    totalScore += gradeToScore[grade] * float(mul)
    totalMul += float(mul)

print(totalScore / totalMul)