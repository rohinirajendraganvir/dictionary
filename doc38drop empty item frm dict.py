a={'c1': 'Red', 'c2': 'Green', 'c3': None}
x={}
for k, v in a.items():
    if v!=None:
        x[k]=v

print(x)
