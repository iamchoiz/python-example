a = 10
if a<0 and 2** a > 1000 and a%5 == 2 and round(a) == a:
    print('???')


def return_false():
    print('함수 return false')
    return False
def return_true():
    print('함수 return true')
    return True

a = return_false()
b = return_true()
print('테스트 1')
if a and b:
    print(True)
else:
    print(False)


print('테스트 2')
# 단락 평가
if return_false() and return_true(): # 어차피 False이기 때문에 뒤에 return_true를 실행 하지 않음
    print("True")
else:
    print(False)

