
class Human():
    '''사람'''


person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = 'English'

person1.name = 'seoul'
person2.name = 'india'

def speak(person):
    print("{}이 {}로 말 합니다.".format(person.name,person.language))


Human.spea = speak
person1.spea()
person2.spea()