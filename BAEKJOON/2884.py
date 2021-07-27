H,M=input().split()
H=int(H)
M=int(M)
if M-45>=0:
    M=M-45
    print(H, M)
elif H-1<0:
    H=23
    M=15+M
    print(H, M)
else:
    H=H-1
    M=15+M
    print(H, M)
