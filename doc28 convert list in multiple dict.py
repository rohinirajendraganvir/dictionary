a = [1, 2, 3, 4]
b = current = {}
for name in a:
    current[name] = {}
    current = current[name]
print(b)


# d= {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# for i in d:
#     d[i]=sorted(d[i])
# print(d)