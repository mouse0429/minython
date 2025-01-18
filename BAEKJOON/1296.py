import sys

name = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
L = name.count("L")
O = name.count("O")
V = name.count("V")
E = name.count("E")

answerScore = 0
answer = ""

for _ in range(N):
    cand = sys.stdin.readline().rstrip()
    cL = L + cand.count("L")
    cO = O + cand.count("O")
    cV = V + cand.count("V")
    cE = E + cand.count("E")
    score = ((cL + cO) * (cL + cV) * (cL + cE) *
             (cO + cV) * (cO + cE) * (cV+cE)) % 100
    if answerScore < score or answer == "" or (answerScore == score and cand < answer):
        answer = cand
        answerScore = score

print(answer)
