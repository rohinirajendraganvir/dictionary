a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
res=[]
for i,j in a.items():
    for k in j:
        d={i:k}
        res.append(d)
print(res)