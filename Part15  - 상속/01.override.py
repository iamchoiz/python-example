class Animal():
    def walk(self):
        print('걷는다')
    def eat(self):
        print('먹는다')
    def greet(self):
        print('인사한다')

class Cow(Animal):
    '''소'''


class Human (Animal): # Animal Class 상속
    def wave(self):
        print('손을 흔든다')
    def greet(self):
        self.wave()

class Dog (Animal): # Animal Class 상속
    def wave(self):
        print('꼬리를 흔든다')
    def greet(self):
        self.wave()

person = Human()
person.greet()

dog = Dog()
dog.greet()

cow = Cow()
cow.greet()