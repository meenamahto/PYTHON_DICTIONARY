dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
dic1={}
for i in (dic):
    dic1.update({i:dic[i]})
print(dic1)