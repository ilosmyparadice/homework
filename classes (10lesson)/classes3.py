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

    def get_kg(self):
        return self.__kg

    def set_kg(self, new_kg):
        if isinstance(new_kg, int | float):
            self.__kg = new_kg
        else: raise ValueError("Килограммы задаются только числами")

smthg = KgToPounds(10)
print(smthg.to_pounds())
smthg.set_kg(5)
print(smthg.get_kg())
print(smthg.to_pounds())
smthg.set_kg("1zgf")

















