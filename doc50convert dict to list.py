# d = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

# l1 = []
# l2 = []

# for v,k in d.items():
#     l1.append(v)
#     l2.append(k)

# res =list(zip(l1,l2))

# print(res)


# def test(dictt):
a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
r = []
for i,j in a.items():
    for k in j:
        if k%2 == 0:
            r.append({i: k})
        print(r)