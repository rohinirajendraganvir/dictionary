l=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

# a,b=l
# ans1={}
# ans2={}
# final_list=[]
# for i,j in a.items():
#     d={i:int(j)}
#     ans1.update(d)
#     for i,j in b.items():
#         d1={i:int(j)}
#         ans2.update(d1)
#         final_ans=ans1,ans2
#         for i in final_ans:
#             final_list.append(i)
# print(ans1)
ans1={}
ans2={}
c=[]
a,b=l
# for i,j in a.items():
#     d={i:float(j)}
#     ans1.update(d)
# print(ans1)
for i,j in b.items():
        d1={i:int(j)}
        ans2.update(d1)
        c=ans1,ans2
        for k in c:
            c.append(k)
print(c)
    