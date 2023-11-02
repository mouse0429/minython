import sys


def canCompress(img, N):
    number = 0
    for i in range(N):
        number += img[i].count('0')
    if (number == 0 or number == N**2):
        return True
    else:
        return False


def checkBound(N, img):
    if N == 1:
        return img[0][0]
    else:
        if canCompress(img, N):
            return img[0][0]
        else:
            result = "("
            newN = N//2
            leftTop = [[img[i][j] for j in range(newN)] for i in range(newN)]
            result += checkBound(newN, leftTop)

            rightTop = [[img[i][j+newN]
                         for j in range(newN)] for i in range(newN)]
            result += checkBound(newN, rightTop)

            leftBot = [[img[i+newN][j]
                        for j in range(newN)] for i in range(newN)]
            result += checkBound(newN, leftBot)

            rightBot = [[img[i+newN][j+newN]
                         for j in range(newN)] for i in range(newN)]
            result += checkBound(newN, rightBot)

            result += ")"
            return result


N = int(sys.stdin.readline())
img = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

result = ""
print(checkBound(N, img))
