ages = {'Tod' : 23, 'A' : 1, 'B' : 2}


for key in ages.keys():
    print('{}의 나이는 {} 입니다.'.format(key,ages[key]))

for key,value in ages.items():
    print('{}의 나이는 {} 입니다.'.format(key,value))

# for value in ages.values():
#     print(value)

