d = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
c=[]
a = max(d,key=d.get)
b = min(d,key=d.get)
d=a,b
c.append(d)
print(c)