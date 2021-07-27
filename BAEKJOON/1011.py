import sys
T=int(sys.stdin.readline())
for _ in range(T):
    x,y=map(int,sys.stdin.readline().split())
    D=y-x
    k,i,num = 0,0,0
    while k<=(D//2):
       i+=1
       k+=i
    num=i-1
    k-=i
    i-=1
    if D-k*2==0:
        print(num*2)
    elif D-k*2<=i+1:
        print(num*2+1)
    else:
        print(num*2+2)

'''
절반으로 나눈 거리 값보다 작을 때까지 1+2+3... 더해감
거리 값에서 더한 값의 두배를 뺐을 때 결과가
0이면 1+2+3+3+2+1 이런식인거고
i+1보다 작거나 같으면 1+2+3+4+3+2+1
i+1보다 크면 1+2+3+5+3+2+1 이런식이니 i보다 작은 수 두가지의 조합으로 나타냄
어차피 1+2+3+1+3+2+1 이나와도 1이 있는 쪽 아무곳에나 끼워 넣으면 되니까
무관해짐
'''
