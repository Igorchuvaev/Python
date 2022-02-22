# 1.

# class Date:
#     def __init__(self, full_date):
#         self.full_date = str(full_date)
#
#     @classmethod
#     def recept(cls, full_date):
#         date = []
#         for i in full_date.split('-'):
#             date.append(i)
#         return int(date[0]), int(date[1]), int(date[2])
#
#     @staticmethod
#     def control(day, month, year):
#         if 0 < day < 32:
#             if 0 < month < 13:
#                 if 2100 > year > 0:
#                     return f"Дата соответствует запросу"
#                 else:
#                     return f"Введен неверный год"
#             else:
#                 return f"Введен неверный месяц"
#         else:
#             return f"Введен неверный день"
#
#     def __str__(self):
#         return f"Текущая дата {Date.recept(self.full_date)}"
#
#
# print(Date.control(12, 2, 2022))

# 2.

# class MyDivision(Exception):
#     # def __init__(self, divisible, divider):
#     #     self.divisible = divisible
#     #     self.divider = divider
#     pass
#
#
# try:
#     divisible = float(input("Введите делимое: "))
#     divider = float(input("Введите делитель: "))
#
#     if divider == 0:
#         raise MyDivision
#     print(f"Деление двух введенных чисел равно {round(divisible / divider, 2)}")
# except:
#     print("Вы ввели в делителе 0, а на ноль делить нельзя")


# 3.

# class Exc3:
#     def __init__(self, *args):
#         self.numbers = []
#
#     def number_list(self):
#         while True:
#             try:
#                 numb = int(input("Введите число: "))
#                 self.numbers.append(numb)
#                 print(f"Список введенных вами чисел \n{self.numbers}\n")
#             except:
#                 print("Вы ввели неверное значение")
#                 decision = input("Для завершения процесса введите: stop\n"
#                                  "Или любой символ для продолжения\n").lower()
#                 if decision == "stop":
#                     return "Процесс завершен"
#
#                 else:
#                     print(my_list.number_list())
#
#
# my_list = Exc3()
# print(my_list.number_list())

# 7.
#
# import math
#
#
# class ComplexNumber:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return '(%s+%si)' % (self.a, self.b)
#
#     def __add__(self, other):
#         a_1 = self.a + other.a
#         b_1 = self.b + other.b
#         return ComplexNumber(a_1, b_1)
#
#     def __mul__(self, other):
#         a_1 = self.a * other.a - self.b * other.b
#         b_1 = self.b * other.a + self.a * other.b
#         return ComplexNumber(a_1, b_1)
#
#
# final_a = ComplexNumber(int(input("Первое число: ")), int(input("Второе число: ")))
# final_b = ComplexNumber(int(input("Первое число: ")), int(input("Второе число: ")))
#
# print("z1 =", final_a + final_b)
# print("z2 =", final_a * final_b)

# 4-6.

# class Equipment:
#     def __init__(self, name, price, quantity, numb, *args):
#         self.name: str = name
#         self.price: int = price
#         self.quantity: int = quantity
#         self.numb = numb
#         self.warehouse = []
#         self.warehouse_full = []
#         self.goods = {"Производитель": self.name, "Стоимость": self.price, "Остаток": self.quantity}
#
#     def __str__(self):
#         return f"Производитель: {self.name}, стоимость: {self.price}, товарный остаток: {self.quantity}"
#
#     def acceptance_goods(self):
#         # while True:
#         try:
#             good_name = input("Введите производителя: ")
#             good_price = int(input("Введите стоимость: "))
#             good_quantity = int(input("Введите остаток: "))
#             good = {"Производитель": good_name, "Стоимость": good_price, "Остаток": good_quantity}
#             self.goods.update(good)
#             self.warehouse_full.append(self.goods)
#             print(f"{self.warehouse_full}")
#         except:
#             return f"Ошибка!"
#
#         decision = input("Для завершения процесса введите: stop\n"
#                          "Или любой символ для продолжения\n").lower()
#
#         if decision == "stop":
#             self.warehouse.append(self.warehouse_full)
#             print(f"На данный момент на складе находятся следующие товары\n"
#                   f"{self.warehouse}")
#             return "Процесс завершен"
#         else:
#             return Equipment.acceptance_goods(self)
#
#
# class Printer(Equipment):
#     def print_count(self):
#         return f"{self.numb}"
#
#
# class Scanner(Equipment):
#     def print_count(self):
#         return f"{self.numb}"
#
#
# class Xerox(Equipment):
#     def print_count(self):
#         return f"{self.numb}"
#
#
# good_1 = Printer(input("Название "), int(input("Стоимость ")), int(input("Остаток ")), int(input("Остаток ")))
# good_2 = Scanner(input("Название "), int(input("Стоимость ")), int(input("Остаток ")), int(input("Остаток ")))
# good_3 = Xerox(input("Название "), int(input("Стоимость ")), int(input("Остаток ")), int(input("Остаток ")))
