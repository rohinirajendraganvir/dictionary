# number = int(input("Please enter the Maximum Number : "))
# myDict = {}

# for i in range(1, number + 1):
#     myDict[i] = i * i
    
# print("dictionary", myDict)


l=[
 {"first":"1"}, 
 {"second": "2"}, 
 {"third": "1"}, 
 {"four": "5"}, 
 {"five":"5"}, 
 {"six":"9"},
{"seven":"7"}
]
dic = []
for i in l:
    for j in i.values():
        if j not in dic:
            dic.append(j)

print(set(dic))