"""В следующих заданиях требуется реализовать абстрактный базовый класс, определив в нем
абстрактные методы и свойства. Эти методы определяются в производных классах. В базовых
классах должны быть объявлены абстрактные методы ввода/вывода, которые реализуются в
производных классах.
Вызывающая программа должна продемонстрировать все варианты вызова переопределенных
абстрактных методов. Написать функцию вывода, получающую параметры базового класса по
ссылке и демонстрирующую виртуальный вызов.

Создать абстрактный базовый класс Figure с абстрактными методами вычисления площади
и периметра. Создать производные классы: Rectanglе (прямоугольник), Circle (круг),
Trapezium (трапеция) со своими функциями площади и периметра. Самостоятельно
определить, какие поля необходимы, какие из них можно задать в базовом классе, а какие —
в производных. Площадь трапеции:
"""
from abc import ABC, abstractmethod
import math

class Figure(ABC):
    """
    Абстрактный базовый класс для фигуры.
    """
    @abstractmethod
    def area(self):
        """
        Метод для вычисления площади.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Метод для вычисления периметра.
        """
        pass

    @abstractmethod
    def display(self):
        """
        Метод для вывода результатов на экран.
        """
        pass

class Rectangle(Figure):
    """
    Класс прямоугольника, наследуется от Figure.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print(f"Прямоугольник со сторонами {self.length} и {self.width} имеет площадь {self.area()} и периметр {self.perimeter()}.")

class Circle(Figure):
    """
    Класс круга, наследуется от Figure.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display(self):
        print(f"Круг с радиусом {self.radius} имеет площадь {self.area():.2f} и периметр {self.perimeter():.2f}.")

class Trapezium(Figure):
    """
    Класс трапеции, наследуется от Figure.
    """
    def __init__(self, a, b, c, d, height):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.height = height

    def area(self):
        return ((self.a + self.b) / 2) * self.height

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def display(self):
        print(f"Трапеция со сторонами {self.a}, {self.b}, {self.c}, {self.d} и высотой {self.height} имеет площадь {self.area()} и периметр {self.perimeter()}.")

def demonstrate_virtual_call(figure):
    """
    Функция для демонстрации использования классов фигур.
    """
    figure.display()

if __name__ == "__main__":
    rectangle = Rectangle(10, 20)
    circle = Circle(5)
    trapezium = Trapezium(3, 5, 4, 6, 4)

    demonstrate_virtual_call(rectangle)
    demonstrate_virtual_call(circle)
    demonstrate_virtual_call(trapezium)