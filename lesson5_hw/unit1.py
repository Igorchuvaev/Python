unit1 = open('unit1.txt', 'w')
print("Введите данные, которые внесутся в unit1.txt,\nчтобы выйти - 2 раза нажмите Enter!  ")
while True:
    unit_text = input("Введите данные: ")
    unit1.write(unit_text + '\n')
    if unit_text == "":
        break
unit1.close()
