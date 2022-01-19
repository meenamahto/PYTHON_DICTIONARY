a={'S 001': ['Math', 'Science'], 'S  002': ['Math', 'English']}
b=[]
for key in a:
    word=""
    for j in key:
        if j!=" ":
            word+=j
    b.append(word)
print(b)
d={}
for i in b:
    for x,y in a.items():
        d.update({i:y})
print(d)


## in second way:-

student_list = {'S 001': ['Math', 'Science'], 'S  002': ['Math', 'English']}

for key,values in list(student_list.items()):
    word = ""
    for i in key:
        if i != " ":
            word += i
    student_list[word] = student_list.pop(key)
print(student_list)
