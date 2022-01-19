
## in first way:-


num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)



## in second way:-


a=[1,2,3,4]
current={}
new=current
for i in (a):
    current[i]={}
    current=current[i]
print(new)





a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
d=[]
# d3={}

for i in b:
    d3={}
    for j in c:
        d3.update({i:j})
    d.append(d3)
print(d)
d1={}
for x in range(len(d)):
    d1.update({a[x]:d[x]})
print(d1)





