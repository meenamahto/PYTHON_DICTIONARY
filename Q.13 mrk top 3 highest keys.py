my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
b=[]
max=0
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
        s=i
b.append(i)
max1=0
for i in my_dict:
    if my_dict[i]>max1:
        if my_dict[i]!=max:
            max1=my_dict[i]
            p=i
b.append(p)
max2=0
for i in my_dict:
    if my_dict[i]>max2:
        if my_dict[i]!=max and my_dict[i]!=max1:
            max2=my_dict[i]
            n=i
b.append(n)
print(b)

