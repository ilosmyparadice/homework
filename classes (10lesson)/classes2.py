# Требуется проверить, возможно ли из представленных отрезков условной длины
# сформировать треугольник. Для этого необходимо создать класс
# TriangleChecker, принимающий только положительные числа. С помощью
# метода is_triangle() возвращаются следующие значения (в зависимости от
# ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if not isinstance(self.a, int | float):
            return "Нужно вводить только числа!"
        if not isinstance(self.b, int | float):
            return "Нужно вводить только числа!"
        if not isinstance(self.c, int | float):
            return "Нужно вводить только числа!"
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b+ self.c > self.a:
            return "Ура, можно построить треугольник!"
        else: return "Жаль, но из этого треугольник не сделать."

triange = TriangleChecker(3,4,5)
triangel = TriangleChecker(-1,2,5)
tri3angel = TriangleChecker("z",2,3)
tri33angel = TriangleChecker(1,2,"z")

print(triange.is_triangle())
print(triangel.is_triangle())
print(tri3angel.is_triangle())
print(tri33angel.is_triangle())






