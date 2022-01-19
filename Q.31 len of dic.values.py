d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
a={}
for i in d:
    a.update({d[i]:len(d[i])})
print(a)

