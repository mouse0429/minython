s=list(input())
result=0
for i in range(len(s)):
    if ord(s[i])<68:
       result+=3
    elif ord(s[i])<71:
        result+=4
    elif ord(s[i])<74:
        result+=5
    elif ord(s[i])<77:
        result+=6
    elif ord(s[i])<80:
        result+=7
    elif ord(s[i])<84:
        result+=8
    elif ord(s[i])<87:
        result+=9
    else:
        result+=10
print(result)
