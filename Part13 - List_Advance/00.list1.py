def safe_index(my_list, value):
    # 함수를 완성하세요
    if value in my_list:
        return my_list.index(value)
    else:
        return None
print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))


list1 = [123,234,345,456]
list2 = [232,12,13,55,1]

list3 = list1 + list2

print(list3)

list3.extend([9,1,2])

print(list3)

print(list3.index(9),'는 값 9의 배열 자리수')

list3.insert(0,0)

print(list3)

list3.insert(-1,9999)

print(list3)

list3.sort()

print(list3)

list3.reverse()
print(list3)

