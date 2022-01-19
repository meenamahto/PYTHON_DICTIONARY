a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
for i in range(len(a)):
    for j in a[i]:
        a[i][j]=int(a[i][j])
print(a)

