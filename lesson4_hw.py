# 1.
# from sys import argv

# file, hours_worked, rate_per_hour, month_bonus = argv

# print(f"Исходня из введенных вами данных: "
#       f"\nСотрудник отработал {hours_worked} часов,"
#       f"\nпри этом каждый час оплачивался по ставке {rate_per_hour} $,"
#       f"\nтакже ежемесячеый бонус составил {month_bonus} $."
#       f"\nИтоговый месячный доход сотрудника составил: ",
#       (float(hours_worked) * float(rate_per_hour)) + float(month_bonus), "$")

# 2.

start_list = [int(i) for i in input("Введите целые числа через пробел: ").split()]
result_list = []
for i in range(1, len(start_list)):
    if start_list[i] > start_list[i - 1]:
        (result_list.append(start_list[i]))
if len(result_list) > 0:
    print(f"Из введенного вами списка {result_list} больше собсвтенного предыдущего числа")
else:
    print("Вы не ввели ни одного числа, чтобы оно было больше предыдущего.")

# 3.

print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])

# 4.

start_list_numbers = [int(i) for i in input("Введите целые числа через пробел: ").split()]
print("Числа, введенные только один раз: ",
      [i for i in start_list_numbers if start_list_numbers.count(i) == 1])

# 5.

from functools import reduce

print("Произведение всех четных чисел от 100 до 1000 равно\n",
      reduce(lambda x, y: x * y, [i for i in range(99, 1001) if i % 2 == 0]))

# 6.

from itertools import count as gen_count, cycle as gen_cycle

start_count = int(input("Введите число, с которого начнется генерация: "))
final_count = int(input("Введите число, которым генерация закончится: "))
for count in gen_count(start_count):
    if count > final_count:
        break
    else:
        print(count)

break_count = int(input("Для чисел 23, 1, 3, 10, 4, 11 введите число, означающее количество итераций: "))
i = 0
for value in gen_cycle([23, 1, 3, 10, 4, 11]):
    if i > break_count:
        break
    print(value)
    i += 1

# 7.

from math import factorial


def fact(n):
    for i in range(n):
        print(f"Факториал {i} ", end='равен ')
        yield factorial(i)


final_count = int(input("Для получения факториалов от 0 до вашего числа - необходимо его ввести! \nЧисло: "))
for el in fact(final_count + 1):
    print(el)
