my_dict = {'data1':100,'data2':100,'data3':20}
# result=1
# for key in my_dict:    
#     result=result * my_dict[key]

# print(result)

mul=0
for i in my_dict:
    mul=mul+my_dict[i]
print("sum of values=",mul)