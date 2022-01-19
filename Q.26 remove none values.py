a={'c1': 'Red', 'c2': 'Green', 'c3': None}
d={}
for i,j in a.items():
    # if j is not "None":
    if j !=None:
        d.update({i:j})
print(d)


