# 1.

# import time
#
#
# def traffic_change_color():
#     while True:
#         print("Красный свет")
#         time.sleep(7)
#         print("Жёлтый свет")
#         time.sleep(2)
#         print("Зеленый свет")
#         time.sleep(4.5)
#
#
# class TrafficLight:
#     __change_color = "Traffic light"
#
#
# traffic_change_color()


# 2.

# class Road:
#     _length: int = 0
#     _width: int = 0
#     thickness: int = 0
#     mass: int = 0
#
#     def __init__(self, _length, _width, thickness, mass):
#         self._length = _length
#         self._width = _width
#         self.thickness = thickness
#         self.mass = mass
#
#     def road_mass(self):
#         length_road = self._length
#         width_road = self._width
#         thickness_road = self.thickness
#         asphalt_mass = self.mass
#         road_mass = length_road * width_road * thickness_road * asphalt_mass
#         return print(f"Исходя из введенных вами данных необходимо {road_mass} кг асфальта")
#
#
# Road(int(input("Введите длину дороги в метрах: ")),
#      int(input("Введите ширину дороги в метрах: ")),
#      int(input("Введите толщину асфальтового покрытия в сантимитрах: ")),
#      int(input("Введите массу асфальта: "))
#      ).road_mass()

# 3.
#
# class Worker:
#     def __init__(self, firstname: str, lastname: str, position: str, income):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.position = position
#         self._income_wage = income["Оклад"]
#         self._income_bonus = income["Премия"]
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return print(f"Сотрудник {self.lastname} {self.firstname} "
#                      f"занимает должность: {self.position}.")
#
#     def get_total_income(self):
#         return print(f"Общий доход сотрудника составляет: "
#                      f"{self._income_wage + self._income_bonus} руб.")
#
#
# worker = Position(input("Введите имя сотрудника: "),
#                   input("Введите фамилию сотрудника: "),
#                   input("Введите занимаемую сотрудником должность: "),
#                   {"Оклад": int(input("Введите оклад сотрудника в рублях: ")),
#                    "Премия": int(input("Введите премию сотрудника в рублях: "))})
#
# worker.get_full_name()
# worker.get_total_income()

# 4

# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed: int = speed
#         self.color: str = color
#         self.name: str = name
#         self.is_police: bool = False
#
#     def car_go(self):
#         print(f"{self.name} начал движение.")
#
#     def car_stop(self):
#         print(f"{self.name} начал торможение.")
#
#     def car_direction(self):
#         print(f"{self.name} осуществляет поворот.")
#
#     def car_color(self):
#         print(f"{self.name} окрашен в {self.color} цвет.")
#
#     def show_speed(self):
#         print(f"{self.name} едет со скоростью {self.speed} км/ч")
#
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             print(f"{self.name} превышеат допустимую скорость!")
#
#
# class SportCar(Car):
#     def show_speed(self):
#         if self.speed < 80:
#             print(f"{self.name} стоит прибавить скорость =)")
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             print(f"{self.name} превышеат допустимую скорость!")
#
#
# class PoliceCar(Car):
#     def car_color(self):
#         if self.color != "синий":
#             print("Рекомендуется сменить цвет на синий! ")
#         else:
#             print(f"{self.name} верно окрашен.")
#
#
# # PoliceCar,WorkCar,SportCar - для самостоятельной замены
#
# trial_car = PoliceCar(int(input("Введите скорость автомобиля (км/ч): ")),
#                       input("Введите цвет автомобиля: ").lower(),
#                       input("Введите название автомобиля: "),
#                       True)
# # car_go(),car_stop(),car_direction() - для самостоятельной замены
#
# trial_car.show_speed()
# trial_car.car_color()

# # 5.
#
# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print(f"{self.title} начинает отрисовку.")
#
#
# class Pen(Stationery):
#     def draw(self):
#         if self.title == "ручка":
#             print(f"Запуск отрисовки, используется зеленая {self.title}.")
#         else:
#             print(f"Должна использоваться ручка.")
#
#
# class Pencil(Stationery):
#     def draw(self):
#         if self.title == "карандаш":
#             print(f"Запуск отрисовки, используется желтый {self.title}.")
#         else:
#             print(f"Должен использоваться карандаш.")
#
#
# class Handle(Stationery):
#     def draw(self):
#         if self.title == "маркер":
#             print(f"Запуск отрисовки, используется красный {self.title}.")
#         else:
#             print(f"Должен использоваться маркер.")
#
#
# # Pen ,Pencil ,Handle  - для самостоятельной замены
# writing_device = Stationery(input("Чем будем писать? ").capitalize())
# writing_device.draw()
# print("Поздравления: рисунок готов!")
