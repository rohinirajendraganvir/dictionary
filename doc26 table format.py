my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)



# sample_data = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': True, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'},


# sum = 0
# for i in sample_data:
#     sum = i['success']
# sum +=1
# print('Count for Success is: ',sum)


# counter = 0
# for item in sample_data:
#     if item['id']:
#         counter += 1
# print(counter)