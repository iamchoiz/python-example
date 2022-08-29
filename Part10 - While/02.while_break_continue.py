list1 = [1,2,3,4,5,6,7,8]

for val in list1:
    if val % 3 == 0:
        print(val)
        break

for i in range(10):
    if i%2 != 0: #홀수
        print(i)
        print(i)
        print(i)
        print(i)

for i in range(10):
    if i%2 != 0: #홀수
        continue
    print(i)
    print(i)
    print(i)
    print(i)