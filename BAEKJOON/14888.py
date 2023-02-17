from itertools import permutations

N = int(input())
A = list(map(int, input().split(" ")))
operNum = list(map(int, input().split(" ")))
operType = ["+", "-", "*", "/"]
oper = []
for i in range(4):
  for j in range(operNum[i]):
    oper.append(operType[i])

maxAnswer = None
minAnswer = None

def cal(a, b, oper):
  strToResult = {"+": a+b, "-": a-b, "*": a*b, "/": (lambda a: (abs(a)//b)*(-1) if a < 0 else (abs(a)//b))(a)}
  return strToResult[oper]

operPermu = list(set(permutations(oper, N - 1)))

for i in range(len(operPermu)):
  tempSum = cal(A[0], A[1], operPermu[i][0])
  for j in range(2, N):
    tempSum = cal(tempSum, A[j], operPermu[i][j-1])
  if maxAnswer == None or maxAnswer < tempSum:
    maxAnswer = tempSum
  if minAnswer == None or minAnswer > tempSum:
    minAnswer = tempSum

print(maxAnswer, minAnswer, sep="\n")

