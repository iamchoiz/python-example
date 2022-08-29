list2 = [37,38,39,40, 41]
print(list2)

list2.append(16)
print(list2)


list3 = list2 + [11]

print(list3)

list4 = list3 + list2

print(list4)

n = 37
ownership = n in list4
print(ownership)

if n in list3:
    print('true {} 있음'.format(n))

print(list4)
del list4[1]
print(list4)

list4.remove(40)
print(list4)