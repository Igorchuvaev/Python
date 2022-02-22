lessons_hours = {}

with open("unit6.txt", encoding="utf-8") as unit5_file:
    for item in unit5_file:
        lessons = item.split()
        hours = [int(i[:i.find("(")]) for i in lessons if i.find("(") != -1]
        lessons_hours[lessons[0]] = sum(hours)

print(lessons_hours)
