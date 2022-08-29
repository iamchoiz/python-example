
class Human():
    '''인간'''
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
    
    def speak(self, message):
        print(message)

def eat(self):
    person.weight += 0.1
    print("adasd{} {} 오름".format(self.name, self.weight))

person = Human.create_human('철수', 60.5)
person.eat()
person.walk()
person.walk()

eat(person)
person.speak("안녕하세요") # 저번째 매개변수 self는 안넣아도됨