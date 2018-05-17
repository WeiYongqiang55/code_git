a="cagy"
b=3
c = ""
for i in range(len(a)):
    if ord(a[i]) + b < ord('z'):
        c += chr(ord(a[i]) + b)
    else:
        c += chr(ord(a[i]) + b - 26)
print(c)