from UnexpectedRSPValue import UnexpectedRSPValue

value = '가'

try:
    if value not in ['가위', '바위','보']:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print('에러 발생')

# def sign_up():
#     '''회원가입 함수'''

# try:
#     sign_up()
# except BadUserName:
#     print('이름으로 사용할 수 없는 입력')
# except PassworNotMatched:
#     print('입력한 패스워드가 서로 일치하지 않음')