wintable = {
    '가위' : '보',
    '보' : '주먹',
    '주먹' : '가위'
}

print(wintable['가위'])

def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

def message(result):
    if result == 'draw':
        return '비겼다 !' 
    elif result == 'win':
        return '이겼다!'
    else:
        return '졌다!'

result = rsp('가위','가위')
print(message(result))


dict = {     "이름표"    :    [1,2,3] }
#                           ↑ 값은 리스트를 포함해서 무엇이든 올 수 있습니다.

print( dict["이름표"] )