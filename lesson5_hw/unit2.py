def unit2_count():
    try:
        with open('unit1.txt', 'r') as unit2_file:
            word_lines = unit2_file.readlines()
            print(f"В проверяемом файле {len(word_lines)} строк.")
            for i in range(len(word_lines)):
                word_count = word_lines[i].split()

                print(f"В {i + 1} строке {len(word_count)} сл.")
    except:
        print("К сожалению, неверно указан файл")


unit2_count()
