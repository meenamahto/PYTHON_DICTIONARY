a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# b=[]
# a={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [7, 7, 9]}
c={}
for i in a:
    b=[]
    for j in range(len(a[i])):
        if a[i][j]%2==0:
            b.append(a[i][j])
            c.update({i:b})
        else:
            c.update({i:b})
print(c)
   






