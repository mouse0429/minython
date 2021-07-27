N=int(input())
origin=N
i=0
while True:
    i+=1
    if N<10:
        A='0'
        B=str(N)
    else:
        A=str(int(N/10))
        B=str(N%10)
    new=int(A)+int(B)
    new=new%10
    N=int(B+str(new))
    if N == origin:
        break
print(i)
