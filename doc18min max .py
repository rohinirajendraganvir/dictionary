

my_dict = {
'a':50, 
'b':58, 
'c':56,
'd':40,
'e':100, 
'f':20
}
e=[]
for i in my_dict:
    e.append(my_dict[i])
e.sort(reverse=False)
# print(e[0:8:1])

d={}
for z in e: 
    for k,v in my_dict.items():
        if v==z:
            d[k]=v
print(d.values())