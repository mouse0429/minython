T=int(input())
list=[]
for i in range(T):
    A,B=input().split()
    A=int(A)
    B=int(B)
    list.append(A+B)
for i in range(T):
    print(list[i])
