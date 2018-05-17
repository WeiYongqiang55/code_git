##回文子串
a="abcba"
n=5
for i in range(len(a)):
    if i+n<=len(a):
        b = a[i:i + n]
        c=b[::-1]
        ##print(c)
        if b==c:
            print("YES")
            exit()

    else:
        break

print("NO")