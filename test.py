a=24
b=36
count=0
num=min(a,b)
for i in range(1,num+1):
    if a%i==0 and b%i==0:
       count+=1

print(count)