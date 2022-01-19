my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
b=[]
max=0
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
b.append(max)
max1=0
for i in my_dict:
    if my_dict[i]>max1:
        if my_dict[i]!=max:
            max1=my_dict[i]
b.append(max1)
max2=0
for i in my_dict:
    if my_dict[i]>max2:
        if my_dict[i]!=max and my_dict[i]!=max1:
            max2=my_dict[i]
b.append(max2)
print(b) 



