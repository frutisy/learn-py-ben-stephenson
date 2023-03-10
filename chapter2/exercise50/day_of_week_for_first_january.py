from math import floor

year = int(input("Введите год: "))

dayOfWeek = (year + floor((year - 1) / 4) - floor((year - 1) / 100) +
             floor((year - 1) / 400)) % 7

if dayOfWeek == 0:
    print(f"В {year} году 1 января будет в воскресенье")
elif dayOfWeek == 1:
    print(f"В {year} году 1 января будет в понедельник")
elif dayOfWeek == 2:
    print(f"В {year} году 1 января будет во вторник")
elif dayOfWeek == 3:
    print(f"В {year} году 1 января будет в среду")
elif dayOfWeek == 4:
    print(f"В {year} году 1 января будет в четверг")
elif dayOfWeek == 5:
    print(f"В {year} году 1 января будет в пятницу")
elif dayOfWeek == 6:
    print(f"В {year} году 1 января будет в субботу")
