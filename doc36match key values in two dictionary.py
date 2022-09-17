x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

for key in x.keys():
    if y[key] == x[key]:
        print(key, ' is present in both x and y')
    else:
        print("key error")


# a,b={'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# for k,v in zip(a,b):

#     if a[k]==b[v]:
#         print(k,": is present in both a,b")
    

# a={'c1': 'Red', 'c2': 'Green', 'c3': None}
# x={}
# for k, v in a.items():
#     if v!=None:
#         x[k]=v

# print(x)

