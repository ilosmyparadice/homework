# Необходимо создать класс KgToPounds, в который принимает количество
# килограмм, а с помощью метода to_pounds() они переводятся в фунты.
# Необходимо закрыть доступ к переменной kg.
# Также, реализовать методы:
# - set_kg() - для задания нового значения килограммов (записывать только
# числовые значения),
# - get_kg() - для вывода текущего значения кг.
# Во второй версии необходимо использовать декоратор property для создания
# setter и getter взамен set_kg и get_kg.

class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if not isinstance(new_kg, int | float):
            raise ValueError("Килограммы задаются только числами")
        else:
            self.__kg = new_kg

smthg = KgToPounds(10)
print(smthg.kg)
print(smthg.to_pounds())

smthg.kg = 5
print(smthg.kg)
print(smthg.to_pounds())

smthg.kg = "lol"



