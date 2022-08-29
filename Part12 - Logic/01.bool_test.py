value = input('입력해') or '아무것도 없음'
print('입력받은값', value)

# input에 값이 없을 경우  boolean 이 false이기 때문에 무조건 뒤에 '아무것도 없음' 값을 따름
# or연산의 결과는 앞의 값이 True이면 앞의 값을, 앞의 값이 False이면 뒤의 값을 따릅니다