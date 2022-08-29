rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
list1 = list(range(20))
print(list1)

# 짝수 인덱스만

print(list1[5:15])
print(list1[5:15:2])
print(list1[5:15:3])

print(list1[15:5:-1])

print(list1[::3]) # 전체

print(list1[::-3]) # 전체



list1 = list(range(20))

# new_list가 5, 8, 11, 14의 값을 가지도록 list1을 slice하세요
new_list = list1[5:15:3]

print(new_list)

# reverse_list가 17, 13, 9, 5의 값을 가지도록 list1을 slice하세요
reverse_list = list1[17:4:-4]

print(reverse_list)

list1 = [0, 1, 2, 3, 4, 5]
# list1의 1부터 3까지를 slice를 이용해서 각각 11, 22, 33으로 바꿔보세요.
# 바꾸고 나면 list1은 [0, 11, 22, 33, 4, 5]가 되어야 합니다.
list1[1:4] = [11,22,33]


list2 = [0, 1, 2, 3, 4, 5]
# list2의 1부터 3까지를 del과 slice를 이용해서 지워보세요
# 바꾸고 나면 list2은 [0, 4, 5]가 되어야 합니다.
del list2[1:4]

print("list1 : {}, list2 : {}".format(list1, list2))