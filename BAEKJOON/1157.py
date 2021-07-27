L=[0 for i in range(26)]
s=list(input())
for i in range(len(s)):
    if ord(s[i])<97:
        L[ord(s[i])-65]+=1
    else:
        L[ord(s[i])-97]+=1
index=0
num=0
for i in range(26):
    if L[i]==max(L):
        index=i
        num+=1
if num>1:
    print("?")
else:
    print(chr(index+65))
        
