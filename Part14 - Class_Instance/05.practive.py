"""
다음 코드는 완성된 Human클래스입니다. 19번째 줄에서 person을 Human클래스의 인스턴스로 만들고, person이 2번 걷고 1번 먹도록 만들어 보세요.
"""
class Human():
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
    
    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
    
    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

# 아래에서 person을 이름과 몸무게를 가지는 Human클래스의 인스턴스로 만들어보세요.
person = Human("사람", 60.2)
person.walk()
person.walk()
person.eat()



print(person)