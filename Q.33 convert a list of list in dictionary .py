a=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
'Zachary Simon', 'VII']]
c={}
for i in range(len(a)):
    b=[]
    for j in range(1,len(a[i])):
        b.append(a[i][j])
        c.update({a[i][0]:b})
print(c)

