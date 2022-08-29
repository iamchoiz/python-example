student = ['태영','진우','정현']

for cc, name in enumerate(student):
    print('{}번의 이름은 {}입니다.'.format(cc,name))


student_dict = {"{}번".format(number+1): name for number, name in enumerate(student)}
print(student_dict)

scores = [85,12,55,100,90]

for x,y in zip(student, scores):
    print(x,y)

score_dict = {student : score for student, score in zip(student, scores)}
print(score_dict)

"""
product_list에는 상품의 목록이 들어 있고, price_list에는 각 상품의 가격이 순서대로 들어있습니다. 
딕셔너리 컴프리헨션을 이용해서 product_dict를 상품의 이름을 키로 가지고, 가격을 값으로 가지는 딕셔너리로 만들어보세요.
"""
product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict = {product:price for product,price in zip(product_list,price_list)}


print(product_dict)