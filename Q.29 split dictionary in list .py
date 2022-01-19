d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
a,b=d.values()
l=[]
# c={}
for i in range(len(a)):
    c={}
    for j in d:
        c.update({j: d[j][i]})
    l.append(c)
print(l)


