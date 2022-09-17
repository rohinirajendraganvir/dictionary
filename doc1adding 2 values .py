
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# e={}
# for i in d1:
#     if i not in d2:
#         e[i]=d1[i]
#     else:
#         e[i]=(d1[i]+d2[i])
#         for x in d2:
#             if x not in e:
#                 e[x]=d2[x]
#                 print(e)

list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

dict ={}
for val in list: 
  if val in list: 
    continue 
  else:
    dict.append(val)

print (dict)
