#B2
class Person:
    def __init__(self,name):
        self.name = name
        self.day = 'добрый день'
        self.evening = 'добрый вечер'
    def good_day(self):
        print(f"{self.name} {self.day}")
    def good_evening(self):
        print(f"{self.name} {self.evening}")
Vasya = Person('Вася')
Vasya.good_day()
Kolya = Person('Коля')
Kolya.good_evening()
