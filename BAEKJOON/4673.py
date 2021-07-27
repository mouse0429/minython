def d(n):
    num = list(str(n))
    for i in range(len(num)):
        n+=int(num[i])
    return n

SelfNum=[i+1 for i in range(10000)]
for i in range(len(SelfNum)):
    try:
        SelfNum.remove(d(i+1))
    except:
        continue
for i in range(len(SelfNum)):
    print(SelfNum[i])
