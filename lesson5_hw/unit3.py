with open('unit3.txt', 'r+', encoding="utf-8") as unit3_file:
    list_workers = list()
    for i in unit3_file.readlines():
        list_workers.extend(i.rstrip().split(' '))
salary_list = list(map(int, list_workers[1:len(list_workers):2]))
print(f"Средний уровень дохода всех сотрудников составляет: {sum(salary_list) / len(salary_list)}.\n"
      f"Доход следующих сотрудников менее 20 000:")
for i in range(1, len(list_workers), 2):
    a = int(list_workers[i])
    if a < 20000:
        print(list_workers[i - 1])

