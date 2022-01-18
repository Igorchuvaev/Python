# 1.

def dividing(a, b):
    while b != 0:
        print(round(a / b, 2))
        break
    else:
        print("На ноль делить нельзя")


dividing(int(input("Введите число, которое будем делить: ")), int(input("Введите число, на которое будем делить: ")))


# # 2.

def user_info(lastname, name, year_birth, city, email, phone_number):
    return print("Информация о пользователе:\n"
                 f"Фамилия: {lastname}, Имя: {name}, "
                 f"Год рождения: {year_birth}, Город проживания: {city},"
                 f"Электронная почта: {email}, Номер телефона: {phone_number}")


user_info(
    lastname=input("Введите фамилию пользователя: "),
    name=input("Введите имя пользователя: "),
    year_birth=input("Введите год рождения пользователя: "),
    city=input("Введите город проживания пользователя: "),
    email=input("Введите адрес электронной почты пользователя: "),
    phone_number=input("Введите номер телефона пользователя: ")
)


# 3.

def my_func(a, b, c):
    table = [a, b, c]
    new_table = sorted(table, reverse=True)
    print("Сумма двух наибольших введенных чисел равна: ", new_table[0] + new_table[1])


my_func(int(input("Введите первое число: ")),
        int(input("Введите второе число: ")),
        int(input("Введите третье число: ")))


# # 4.1

def func_degree(x, y):
    while x > 0 and y < 0:
        print("Возведение первого числа в степень равной второму: ", round(x ** y, 9))
        break
    else:
        print("Вы ввели числа, не отвечающие требованиям")


func_degree(float(input("Введите положительное число: ")),
            int(input("Введите отрицательное число: ")))


# 4.2

def func_degree_second(x, y):
    num = 1
    for i in range(abs(y)):
        num *= x
    if y < 0 and x > 0:
        print("Возведение первого числа в степень равной второму = ", round(1 / num, 9))
    else:
        print("Вы ввели числа, не отвечающие требованиям")


func_degree_second(float(input("Введите положительное число: ")),
                   int(input("Введите отрицательное число: ")))

# 5.

sum_all = 0
relay = True
while relay:
    all_numbers = input("Введите числа через запятую: \n"
                        "Для завершения введите exit: ").split(",")
    for i in all_numbers:
        try:
            sum_all += int(i)
        except ValueError:
            if i == "exit":
                relay = False
                break
            else:
                print("Вы ввели числа, не отвечающие требованиям. Либо ввод был некорректным.")
    print("Сумма всех введенных чисел равна: ", sum_all)


# 6.1


def int_func(text):
    return text.title()


print(int_func(input("Введите слово либо текст для конвертации: ")))


# 6.2


def int_func_second(text):
    count = text.count(" ")
    if count > 0:
        return text.title()

    else:
        return text.lower()


print(int_func_second(input("Введите слово либо текст для конвертации: ")))
