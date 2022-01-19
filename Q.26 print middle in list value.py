a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
for i in a:
    for j in a[i]:
        b=a[i][4]
        # if j%5==0:
    print(b)





a=['x','y','z']
d={}
for i in range(3):
    b=[]
    for j in range(10):
        n=int(input("Enter your number:"))
        b.append(n)
    d.update({a[i]:b})
print(d)
