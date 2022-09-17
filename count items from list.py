d = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

count = 0

for i in d:
    for x in d[i]:
        count +=1
print("total count=",count)