A,B = map(int, input().split())
C=int(input())
changeToMinute = A*60+B+C
if changeToMinute >= 1440:
    changeToMinute -= 1440
print(changeToMinute//60, changeToMinute%60)