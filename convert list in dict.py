
li=[1,"a",2,"b",3,"c"]
# o/p={1:'a',2:'b',3:'c'}
d={}
x=1
for i in range(0,len(li),+2):
    d[li[i]]=li[x]
    x+=2
print(d)


