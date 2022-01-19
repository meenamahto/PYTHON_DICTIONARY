a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary,Simon']}
c=[]
b={}
for i in a:
    for j in range(len(a[i])):
        b.update({i:a[i][j]})
c.append(b)
print(c)





def check(a):
    c=[]
    b={}
    for i in a:
        for j in range(len(a[i])):
            b.update({i:a[i][j]})
    c.append(b)
    print(c)
check(a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary,Simon']})

