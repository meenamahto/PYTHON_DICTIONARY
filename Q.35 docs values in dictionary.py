d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
b=[]
a=({d[i][j] for i in range(len(d)) for j in d[i] })
print(a)