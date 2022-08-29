""" 튜플은 한번 만들면 수정이 불가능함"""
tuple1 = (1,2,3)


a,b = 1,2
print(a,b)

#packing unpacking

c = (3,4)
print(c)
d, e = c
print(d,e)

f = d,e
print(f)

# 데이터 값 서로 변경 할때 유용
x = 5
y = 10
print(x,y)
y, x = x,y
print(x,y)

def tuple_func():
    return 1,2

q,w = tuple_func()
print(q,w)