# def rsp(mine, yours):
#     allowed = ['가위', '바위', '보']
#     if mine not in allowed:
#         raise ValueError
#     if yours not in allowed:
#         raise ValueError
    
# try:
#     rsp('가위','바')
# except ValueError:
#     print("ex")    

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
for shop, products in shops.items():
    for product,price in products.items():
        if product == '풀':
            print(shop)


shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product =='풀':
                print("{}: {}원".format(shop, price))
                raise StopIteration
                
except StopIteration:
    print('StopIteration')