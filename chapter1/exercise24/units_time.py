SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

time = input("Введите временной промежуток в d:h:m:s формате: ").split(":")

timeInSeconds = int(time[0]) * SECONDS_IN_DAY + \
                int(time[1]) * SECONDS_IN_HOUR + \
                int(time[2]) * SECONDS_IN_MINUTE + \
                int(time[3])

print(f"Время в секундах равно {timeInSeconds}")
