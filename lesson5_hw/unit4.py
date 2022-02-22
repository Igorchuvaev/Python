with open('unit4.txt', 'r+', encoding="utf-8") as unit4_file:
    list_numbers_eng = list()
    for i in unit4_file.readlines():
        list_numbers_eng.extend(i.split(' '))
# print(list_numbers_eng)

list_numbers_rus = ["Один", "Два", "Три", "Четыре"]

k = 0
for j in range(0, len(list_numbers_eng), 3):
    list_numbers_eng[j] = list_numbers_rus[k]
    k += 1

# print(list_numbers_eng)
with open('unit4_rus.txt', 'w', encoding="utf-8") as rus_numb:
    rus_numb.writelines(list_numbers_eng)
    for x in list_numbers_rus:
        rus_numb.write(str(x) + '\n')
