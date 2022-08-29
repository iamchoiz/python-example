class Animal():
    def __init__(self,name):
        self.name = name

    def walk(self):
        print('걷는다')
    def eat(self):
        print('먹는다')
    def greet(self):
        print('{}이 인사한다'.format(self.name))

class Human (Animal): # Animal Class 상속
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand
    def wave(self):
        print('{}을 손을 흔들면서'.format(self.hand))
    def greet(self):
        self.wave()
        super().greet() # overrided에서 부모 메서드도 실행

person = Human("사람","오른손")
person.greet()
