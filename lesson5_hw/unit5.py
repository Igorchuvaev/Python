def unit5_count():
    try:
        with open('unit5.txt', 'w+') as unit5_file:
            unit5_file.write(input("Введите числа через пробел: "))
            count = map(int, unit5_file.read().split())


    except:
        print("К сожалению, неверно указан файл")


unit5_count()
sum_all = 0
with open('unit5.txt', 'r+', encoding="utf-8") as unit5_file_ch2:
    for i in unit5_file_ch2.read().split():
        sum_all += int(i)
if sum_all > 0:
    print(f"Сумма всех чисел, находящихся в unit5.txt, равна: {sum_all}")
else:
    print("В файле unit5.txt либо нет значений, либо они нулевые! ")
