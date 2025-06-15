# Строки в Питоне сравниваются на основании значений символов. Т.е. если мы
# захотим выяснить, что больше: Apple или Яблоко, – то Яблоко окажется
# бОльшим. А все потому, что английская буква A имеет значение 65 (берется из
# таблицы кодировки), а русская буква Я – 1071. Надо создать новый класс
# RealString, который будет принимать строку и сравнивать по количеству
# входящих в них символов. Сравнивать между собой можно как объекты класса,
# так и обычные строки с экземплярами класса RealString.

from functools import total_ordering

@total_ordering
class RealString:
    def __init__(self, string):
        self.string = string
        self.length = len(self.string)

    def __eq__(self, other):
        if isinstance(other, RealString):
            return self.length == other.length
        elif isinstance(other, str):
            return self.length == len(other)
        raise TypeError('Это мы не поддерживаем')




    def __lt__(self, other):
        if isinstance(other, RealString):
            return self.length < other.length
        elif isinstance(other, str):
            return self.length < len(other)
        raise TypeError('Это мы не поддерживаем')



string11 = RealString('Яблоко')
string12 = RealString('Апельсин')

print(string11 < string12)
print(string11 > "Анананас")
print(string12 < 111)