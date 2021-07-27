import sys
L=[]
for i in range(int(input())):
    age,name=map(str,sys.stdin.readline().split())
    L.append([int(age),name,i])
L= sorted(L,key=lambda x:(x[0],x[2]))
for i in range(len(L)):
    print(L[i][0], L[i][1])
