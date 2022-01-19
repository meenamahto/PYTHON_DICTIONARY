s = {'Aex':{'class':'V',
'rolld_id':2},
'Puja':{'class':'V',
'roll_id':3}}


##in one way:-

for key,value in s.items():
    print(key)
    if type(value)==dict:
        for i in value:
            print(i,':',value[i])


##in second way:-

for i in s:
    print(i)
    for j in s[i]:
        print(j,":",s[i][j])
