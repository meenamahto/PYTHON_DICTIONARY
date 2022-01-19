a=[{'id': 1, 'success': True, 'name': 'Lary'},
{'id': 2, 'success': False, 'name': 'Rabi'},
{'id': 3, 'success': True, 'name': 'Alex'}]
sum=0
for i in range(len(a)):
    for j in (a[i]):
        if type(a[i][j]) ==int:
            sum=sum+a[i][j]
print(sum)
