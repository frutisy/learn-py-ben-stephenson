SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

timeInSeconds = int(input("Введите время (в секундах): "))

days = 0
hours = 0
minutes = 0
seconds = 0

while timeInSeconds != 0:

    if timeInSeconds >= SECONDS_IN_DAY:
        days += 1
        timeInSeconds -= SECONDS_IN_DAY

    elif SECONDS_IN_DAY > timeInSeconds >= SECONDS_IN_HOUR:
        hours += 1
        timeInSeconds -= SECONDS_IN_HOUR

    elif SECONDS_IN_HOUR > timeInSeconds >= SECONDS_IN_MINUTE:
        minutes += 1
        timeInSeconds -= SECONDS_IN_MINUTE

    elif SECONDS_IN_MINUTE > timeInSeconds:
        seconds = timeInSeconds
        timeInSeconds -= seconds

if hours < 10 and minutes < 10 and seconds < 10:
    print(f"{days}:0{hours}:0{minutes}:0{seconds}")


elif hours >= 10 and minutes < 10 and seconds < 10:
    print(f"{days}:{hours}:0{minutes}:0{seconds}")

elif hours < 10 and minutes >= 10 and seconds < 10:
    print(f"{days}:0{hours}:{minutes}:0{seconds}")

elif hours < 10 and minutes < 10 and seconds >= 10:
    print(f"{days}:0{hours}:0{minutes}:{seconds}")


elif hours >= 10 and minutes >= 10 and seconds < 10:
    print(f"{days}:{hours}:{minutes}:0{seconds}")

elif hours >= 10 and minutes < 10 and seconds >= 10:
    print(f"{days}:{hours}:0{minutes}:{seconds}")

elif hours >= 10 and minutes < 10 and seconds >= 10:
    print(f"{days}:{hours}:0{minutes}:{seconds}")


else:
    print(f"{days}:{hours}:{minutes}:{seconds}")
