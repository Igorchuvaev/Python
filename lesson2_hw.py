# 1.
man_name = "Ivan Petrov"
mane_age = 30
man_direction = {'city': 'Moscow', 'country': 'Russia'}
man_house = ['Arbat', '4']
man_car = ('Audi', '8')
man = [man_name, mane_age, man_direction, man_house, man_car]
for i in man:
    print("{} ".format(i), f"{type(i)}")

# 2.

number = int(input("Введите количество элементов в списке: "))
list = []
index = 0
while index < number:
    list.append(input("Введите {} необходимых(ый) значений в списке: ".format(number)))
    index += 1
print(list)
value = 0
for index in range(int(len(list) / 2)):
    list[value], list[value + 1] = list[value + 1], list[value]
    value += 2
print(list)

# 3.
# num = int(input("Введите номер месяца (от 1 до 12): "))
# if 12 >= num >= 1:
#     dict_months = {1: 'январь (зима) ',
#                    2: 'февраль (зима)',
#                    3: 'март (весна)',
#                    4: 'апрель (весна)',
#                    5: 'май (весна)',
#                    6: 'июнь (лето)',
#                    7: 'июль (лето)',
#                    8: 'август (лето)',
#                    9: 'сентябрь (осень)',
#                    10: 'октябрь (осень)',
#                    11: 'ноябрь (осень)',
#                    12: 'декабрь (зима)'}
#     list_months = list(dict_months.values())
#     print(f"Введенный номер соответствует месяцу: {list_months[num - 1]}")
# else:
#     print("Месяца с таким номером не существует")

# 4.

import re

text = input("Введите текст: ")
words = re.split(r"[ ; , , : , - ]", text)
for number, word in enumerate(words):
    if len(word) > 10:
        word = word[:10]
    print(f"№{number+1}  {word}")

# 5.

numbers_list = [5, 4, 3, 2, 1]
print("Существует набор натуральных чисел: ", numbers_list)
num = int(input("Введите число: "))
count = numbers_list.count(num)
print("Вы ввели число, которое встречается в списке", f"{count}", "раз")
for number in numbers_list:
    if count:
        i = numbers_list.index(num)
        numbers_list.insert(i + count, num)
        break
    else:
        if num > number:
            j = numbers_list.index(number)
            numbers_list.insert(j, num)
            break
        else:
            numbers_list.append(num)
            break
print(numbers_list)

# 6.

products = []
while input("Заведем товар: да/нет? ") == "да":
    article_prod = int(input("Артикул: "))
    properties = {}
    name_prod = input("Название: ")
    price_prod = input("Стоимость: ")
    count_prod = input("Товарный остаток: ")
    products.append(tuple([article_prod, properties]))
table = {"Название": [], "Стоимость": [], "Товарный остаток": []}
if products:
    table["Название"].append(name_prod)
    table["Стоимость"].append(price_prod)
    table["Товарный остаток"].append(count_prod)
print(table)
