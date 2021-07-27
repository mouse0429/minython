s=list(input())
num=0
i=0
while i < len(s):
    if s[i] == 'c':
        try:
            if (s[i+1]=='=') | (s[i+1]=='-'):
                i+=1
        except:
            num+=1
            i+=1
            continue
    elif s[i] == 'd':
        try:
            if s[i+1]=='-':
                i+=1
            elif (s[i+1]=='z') & (s[i+2]=='='):
                i+=2
        except:
            num+=1
            i+=1
            continue
    elif s[i] == 'l':
        try:
            if s[i+1]=='j':
                i+=1
        except:
            num+=1
            i+=1
            continue
    elif s[i] =='n':
        try:
            if s[i+1]=='j':
                i+=1
        except:
            num+=1
            i+=1
            continue
    elif s[i] =='s':
        try:
            if s[i+1]=='=':
                i+=1
        except:
            num+=1
            i+=1
            continue
    elif s[i] == 'z':
        try:
            if s[i+1]=='=':
                i+=1
        except:
            num+=1
            i+=1
            continue
    i+=1
    num+=1
print(num)
