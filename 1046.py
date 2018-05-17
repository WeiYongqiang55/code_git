n = int(input())
x=y=0
for i in range(n):
    L = str(input())
    L=L.split(' ')
    a1=int(L[0])
    a2=int(L[1])
    b1=int(L[2])
    b2=int(L[3])
    if(a2==a1+b1 and a2!=b2):
        x=x+1
    if(b2==a1+b1 and a2!=b2):
        y=y+1
print("%d %d "%(y,x))
