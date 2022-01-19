d={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
c1,c2,c3=d.values()
print("c1","c2","c3")
for i in range(len(c1)):
    for j in range(len(c2)):
        for k in range(len(c3)):
            if i==j and j==k:
                print(c1[i],c2[j],c3[k])

