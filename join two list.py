dict1={"a":"rohini","b":"laxmi"}
dict2={"n":"manpret","m":"nikita"}
dict1.update(dict2)
print(dict1)

a=[]
for i in dict1.values():
    a.append(i)
    b=[]
    for j in dict2.values():
        b.append(j)
    # c=a+b
print(a+b)