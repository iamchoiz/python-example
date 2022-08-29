my_list = [0,1,2,3]

print(my_list[0])

str = "Hello World"

print(str[0])

print(3 in my_list)

print('H' in str)

print(my_list.index(2))
print(str.index("o"))

word = "Hello World 안녕 하세요"
word_list = word.split()
print(word_list)

time_str = "10:35:12"
time_str_list = time_str.split(':')
print(time_str_list)

# 다시 변경
time_str_list = ":".join(time_str_list)
print(time_str_list)