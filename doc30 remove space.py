student_list= {'S  001': ['Math', 'Science'], 'S  002': ['Math', 'English']}
d={}

for k,v in student_list.items():
    x=''
    for i in k:
        if i.isspace():
            continue
        x+=i
    d[x] = v
print(d)


# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key value count")
# count=1
# for i in (dict_num):
#     # count+=1
#     print(i,' ',dict_num[i],' ',count)
# count+=1
