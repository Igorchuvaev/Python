# 1.
a = int(input("Введите целое число: "))
print("Вы ввели ", a)
b = a * 10
print("Ваше число, умноженное на 10, равно", b)

# 2.
second = int(input("Введите необходимое количество секунд: "))
hour = second // 3600
minute = (second - hour * 3600) // 60
second = (second - hour * 3600 - minute * 60)
print("В введенном количестве секунд {} час(ов), {} минут, {} секунд".format(hour, minute, second))

# 2. вариант 2
import time
n = int(input("Введите необходимое количество секунд: "))
print(time.strftime("%H:%M:%S", time.gmtime(n)))

# 3.
n = int(input("Введите целое число n: "))
m = n * 10 + n
k = n * 100 + m
z = k + m + n
print("По формуле `nnn+nn+n` результат равен {}+{}+{}={}".format(k, m, n, z))
print(z)

# 4.
number = abs(int(input("Введите целое положительное число: ")))
if number // 10 < 1:
    print("Вы ввели однозначное число: ", number)
else:
    max_count = number % 10
    while number >= 1:
        number = number // 10
        if number % 10 > max_count:
            max_count = number % 10
        if max_count > 9:
            continue
        else:
            print("Максимальная цифра в числе", max_count)
            break
# 5.
revenue = int(input("Введите значение выручки компании: "))
cost = int(input("Введите значение издержек компании: "))
if revenue - cost > 0:
    numb_people = int(input("Введите количество человек в фирме: "))
    print("Прибыль компании составила ", revenue - cost,
          "\nЕё рентабельность составила ", round(((revenue - cost) / revenue), 2),
          "\nПрибыль на каждого сотрудника составила ", round(((revenue - cost) / numb_people), 2))
else:
    print("К сожалению, вы работаете в минус")

# 6.
a = int(input("Введите значение начальное количество километров: "))
b = int(input("Введите желаемый результат: "))
if b < a:
    print("На сегодняшний день результат достигнут")
count = 1
while a < b:
    a = a + a * 0.1
    count += 1
    print("На {}й день:".format(count), round(a, 2))
    if a > b:
        print("На {}й день спортсмен достигнет поставленного результата".format(count))
