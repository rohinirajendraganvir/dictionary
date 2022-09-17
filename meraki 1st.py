# city_population = {
# "NewYorkCity":8550405,
# "LosAngeles":3971883, 
# "Toronto":2731571, 
# "Chicago":2720546, 
# "Houston":2296224, 
# "Montreal":1704694, 
# "Calgary":1239220, 
# "Vancouver":631486, 
# "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))


# Dict = {
#    'ball' : 'green',
#    'Ball': 'red'
#  }
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])

# person={
# 'name':'jack',
# 'age':20,
# 'gender':'male',
# 4:'organization'
# }

# result = person['age'] 
# x = person.get('gender')
# print(person[4])
# print(x)
# print(result)

# dic= {
# 'Name': 'RAM', 
# 'Age': 17,
# }

# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic)


# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# c={}
# for i in dic1,dic2,dic3:
#     c.update(i)
# print(c)


# dict1={"name":"Raju", "marks":56}
# user=input("enter the key...")
# if user in dict1.keys():
#     print("exist")
# else:
#     print("not exist")

# my_dict = {
#  'data1':100,
#  'data2': -54,
#   'data3': 247
#   }
# sum=0
# for i in my_dict.values():
#     sum=sum+i
# print(sum)
    

# a={1:"A",2:"B",3:"C"}
# c={}
# for i in a.items():
# #    print(a[i],end=" ")
# # c={}
#     # print(i,end="")

#     for j in i:
#         for k,v in a.items():
#             if v==j:
#                 c[k]=v
# print(c)

# a={1:"A",2:"B",3:"C"}
# d=[]
# for b in a.values():
#     d.append(b)
# c={}
# for l in d:
#     for k,v in a.items():
#         if v==l:
#             c[k]=v
# print(c)
        

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# d={}
# for i in range(len(list1)):
#     d[list1[i]]=list2[i]
# print(d)

# dict1={
#     "ball":"red",
#     "bat":4,
#     "wicket":8,
#     "ball":"green"
# }
# temp = []
# res = dict()
# for key, val in dict1.items():
#     if val not in temp:
#         temp.append(val)
#         res[key] = val
# print(res)
  

# l=[
#  {"first":"1"}, 
#  {"second": "2"}, 
#  {"third": "1"}, 
#  {"four": "5"}, 
#  {"five":"5"}, 
#  {"six":"9"},
# {"seven":"7"}
# ]
# dic = []
# for i in l:
#     for j in i.values():
#         if j not in dic:
#             dic.append(j)

# print(list(dic))



# students = dict()
# n = int(input("Enter number of students :"))
# for i in range(n):
#         sname = input("Enter names of student :")
#         marks= []
#         for j in range(3):
#            mark = float(input("Enter marks :"))
#            marks.append(mark)
#         students[sname] = marks
# print("Dictionary of student created :")
# print(students)

# d = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

# count = 0

# for i in d:
#     for x in d[i]:
#         count +=1
# print("total count=",count)

my_dict = {
'a':50, 
'b':58, 
'c':56,
'd':40, 
'e':100, 
'f':20
}
e=[]
for i in my_dict:
    e.append(my_dict[i])
e.sort(reverse=False)
print(e[::-1])


# n=int(input("enter a num.."))
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)

# d={'bijender':45,'deepak':60,'param':20,"anjili":30,"roshini":50}
# x= sorted(d.items())
# print(x)
# y = x[::-1]
# print(y)

a=[1,2,3,4]
a.extend("pen")
print(a)