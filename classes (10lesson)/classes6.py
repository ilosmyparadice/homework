# Напишите класс Person, который имеет атрибуты name (имя), age (возраст)
# и gender (пол). Класс должен иметь следующие методы:
# • Конструктор, который принимает три параметра: name, age и gender, и
# инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса
# Person в формате “Имя: name, Возраст: age, Пол: gender”.
# • Метод get_name, который возвращает значение атрибута name.
# • Метод set_name, который принимает один параметр: new_name, и
# устанавливает значение атрибута name равн ым new_name. Этот метод
# должен быть декорирован как property.
# • Метод is_adult, который возвращает True, если возраст объекта больше
# или равен 18, и False в противном случае. Этот метод должен быть
# декорирован как staticmethod.
# • Метод create_from_string, который принимает один параметр: s, и
# создает и возвращает объект класса Person на основе строки s. Строка s
# должна иметь формат “name-age-gender”, где name - имя, age - возраст и
# gender - пол. Этот метод должен быть декорирован как classmethod

class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


    @staticmethod
    def is_adult(age):
        return age >= 18


    @classmethod
    def create_from_string(cls, s: str):
        if s:
            name, age, gender = s.split('-')
            return cls(name, age, gender)


p = Person("Анна", 22, "женский")
print(p)
print(p.get_name())

p.name = "Мария"
print(p)

print(Person.is_adult(17))
print(Person.is_adult(25))

s = "Владимир-25-мужской"
p2 = Person.create_from_string(s)
print(p2)
