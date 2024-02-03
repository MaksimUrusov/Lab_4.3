#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Составить программу с использованием иерархии классов. Номер варианта необходимо
получить у преподавателя. В раздел программы, начинающийся после инструкции if __name__
= '__main__': добавить код, демонстрирующий возможности разработанных классов.


Создать класс Pair (пара целых чисел); определить методы изменения полей и операцию
сложения пар (а,b)+(c.b)=(a+b.c+b). Определить класс-наследник Long с полями:
старшая часть числа и младшая часть числа. Перео пределить операцию сложения и
определить методы умножения и вычитания.
"""
class Pair:
    """
    Класс представляет пару целых чисел.
    """
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def read(self):
        self.first = int(input("Введите первое число: "))
        self.second = int(input("Введите второе число: "))

    def display(self):
        print(f"Пара: ({self.first}, {self.second})")

    def __add__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first + other.first, self.second + other.second)
        else:
            raise ValueError("Операнд должен быть экземпляром класса Pair")

class Long(Pair):
    """
    Класс наследник Pair, реализующий длинные числа.
    """
    def __init__(self, first=0, second=0):
        super().__init__(first, second)

    def __add__(self, other):
        # Переопределение операции сложения
        new_first = self.first + other.first
        new_second = self.second + other.second
        # Обработка переполнения
        if new_second >= 100:
            new_first += new_second // 100
            new_second = new_second % 100
        return Long(new_first, new_second)

    def multiply(self, number):
        # Умножение на число
        total_second = (self.first * 100 + self.second) * number
        return Long(total_second // 100, total_second % 100)

    def subtract(self, other):
        # Вычитание чисел
        total_second_self = self.first * 100 + self.second
        total_second_other = other.first * 100 + other.second
        result = total_second_self - total_second_other
        return Long(result // 100, result % 100)

if __name__ == '__main__':
    print("Работа с классом Pair:")
    pair1 = Pair()
    pair1.read()
    pair2 = Pair(3, 4)
    result_pair = pair1 + pair2
    print("Результат сложения пар:")
    result_pair.display()

    print("\nРабота с классом Long:")
    long1 = Long()
    long1.read()
    long2 = Long(3, 75)
    result_long = long1 + long2
    print("Результат сложения длинных чисел:")
    result_long.display()

    print("Результат умножения длинного числа на 2:")
    result_multiply = long1.multiply(2)
    result_multiply.display()

    print("Результат вычитания длинных чисел:")
    result_subtract = long1.subtract(long2)
    result_subtract.display() 