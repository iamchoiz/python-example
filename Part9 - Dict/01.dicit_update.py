wintable = {
    '가위' : '보',
    '보' : '주먹',
    '주먹' : '가위'
}

## 수정
wintable['가위'] = '가위'

print(wintable)

## 추가
wintable['가위바위'] = '보'

print(wintable)

## 삭제
del wintable['가위바위']

print(wintable)

dict1 = {1 : 100, 2:200}
dict2 = {1:1000, 2:300, 3:3000}
dict1.update(dict2)
print(dict1)

products = {"풀":800, "딱풀":1200, "색종이":1000,"색연필":5000,"스케치북":3500}

catalog = {"겨울용 실내화":12000, "잠자리채":8000, "딱풀":1400}

products.update(catalog)
print(products)