from ast import Import


text = '100%'
try:
    number = int(text)
except ValueError:
    print('{}는 숫자가 아니네'.format(text))


def safe_pop_print(list, index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{} indext의 값을 가져올수없음'.format(index))

safe_pop_print([1,2,3],5)


try:
    number = int(text)
except Exception as ex:
    print(ex)


