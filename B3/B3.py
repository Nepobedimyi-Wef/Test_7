#B3
class Message2:
    def __init__(self, name):
        self.__name = name

class Person1(Message2):
    def good_bye(self):
        print(f"{self._Message2__name} пока")

class Person2(Message2):
    def good_bye(self):
        print(f"{self._Message2__name} пока")

class Person3(Message2):
    def good_bye(self):
        print(f"{self._Message2__name} пока")

name1 = input('Введите имя: ')
name2 = input('Введите имя: ')
name3 = input('Введите имя: ')

person1 = Person1(name1)
person2 = Person2(name2)
person3 = Person3(name3)

person1.good_bye()
person2.good_bye()
person3.good_bye()
