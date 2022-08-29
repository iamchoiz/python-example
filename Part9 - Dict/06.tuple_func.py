list1 = [1,2,3,4,5]

for i, v in enumerate(list1): # i,v = tuple
    print('{}번째 값 : {}'.format(i,v))

for a in enumerate(list1): # i,v = tuple
    print('{}번째 값 : {}'.format(a[0],a[1]))

for a in enumerate(list1): # i,v = tuple
    print('{}번째 값 : {}'.format(*a))

ages = {'Tod' : 1, 'Jane' : 2}
for key,val in ages.items():
    print('{}의 나이는{}'.format(key,val))

for a in ages.items():
    print('{}의 나이는{}'.format(*a))
