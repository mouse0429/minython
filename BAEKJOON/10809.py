s=list(input())
a=[-1 for i in range(26)]
for i in range(len(s)):
    if a[ord(s[i])-97]==-1:
        a[ord(s[i])-97]=i
for i in range(26):
    print(a[i], end=" ")
