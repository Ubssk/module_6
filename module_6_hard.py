import math


class Figure:
    sides_count = 0
    def __init__(self, __color, *__sides):
        self.__sides = []
        self.__color = list(__color)
        self.filled = False

        if len(__sides) == self.sides_count:
            if self.__is_valid_sides(*__sides):
                self.__sides = list(__sides)
            else:
                self.__sides = [__sides[0]] * self.sides_count
        else:
            self.__sides = [__sides[0]] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            self.__color = self.__color
            print("Введены некорректные данные, цвет остаётся прежним")

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Стороны не изменятся, введено некорректное количество")

class Circle(Figure):
    sides_count = 1
    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        if len(__sides) == self.sides_count:
            self.__radius = (__sides[0] / 2) * math.pi
        else:
            self.__radius = 1

    def get_square(self, __radius):
        return f"Площадь круга: {math.pi * (self.__radius**2)}"

class Triangle(Figure):
    sides_count = 3
    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        self.__sides = self.get_sides()

    def get_square(self, __sides):
        s = sum(self.__sides) / 2
        return f"Площадь треугольника: {math.sqrt(s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2]))}"

class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        if len(__sides) == 1:
            self.__sides = [__sides[0]] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

    def get_volume(self):
        side_length = self.__sides[0]
        return f"Объем куба: {side_length ** 3}"



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)



# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится

print(cube1.get_color())



# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится

print(cube1.get_sides())

circle1.set_sides(15) # Изменится

print(circle1.get_sides())



# Проверка периметра (круга), это и есть длина:

print(len(circle1))



# Проверка объёма (куба):

print(cube1.get_volume())
