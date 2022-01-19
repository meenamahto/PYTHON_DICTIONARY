

## with inputs:-

string=input("Enter your string:")
string="aabcdcb"
a=string
dict1={}
for i in a:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
print(dict1)



## without inputs:-

a='w3resource'
b=a
d={}
for i in b:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)

