
class Human():
    '''인간'''
    def __init__(self, name, weight):
        '''초기화'''
        print('init 실행')
        self.name = name
        self.weight = weight

    def __str__(self):
        '''문자열화 함수'''
        print('str 실행')
        return "{} 몸무게 {} kg".format(self.name, self.weight)

    def create_human(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat(self):
        person.weight += 0.1
        print("{} {} 오름".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{} {} 떨어짐".format(self.name, self.weight))

person = Human("사람",60.5)
print(person) # __str__ 없으면 <__main__.Human object at 0x100cb9fd0> 형식으로 출력
print(person.weight)
