a={'key1': 1, 'key2': 3, 'key3': 2}
b={'key1': 1, 'key2': 2}
for x,y in a.items():
    for i,j in b.items():
        if x==i and y==j:
            print(y)

