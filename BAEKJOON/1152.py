s=list(input())
num=0
for i in range(len(s)):
    if s[i] == " ":
        num+=1
result = -1
if num == len(s):
    result=0

if s[0]==" ":
    num-=1
if (len(s)>1) & (s[len(s)-1]==" "):
    num-=1

if result != 0:
    result = num+1
print(result)


    
