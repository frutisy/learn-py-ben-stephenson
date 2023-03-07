CHIPPING_HAMMER = 130
GAS_MOWER = 106
ALARM_CLOCK = 70
QUIET_ROOM = 40

noiseLevel = int(input("Введите уровень шума (в дБ): "))

if noiseLevel < QUIET_ROOM or noiseLevel > CHIPPING_HAMMER:
    print(f"Уровень шума ниже минимального ({QUIET_ROOM} дБ) или "
          f"выше максимального ({CHIPPING_HAMMER} дБ)")
else:
    if noiseLevel == CHIPPING_HAMMER:
        print(f"Уровень шума равен {CHIPPING_HAMMER}")
    elif noiseLevel == GAS_MOWER:
        print(f"Уровень шума равен {GAS_MOWER}")
    elif noiseLevel == ALARM_CLOCK:
        print(f"Уровень шума равен {ALARM_CLOCK}")
    elif noiseLevel == QUIET_ROOM:
        print(f"Уровень шума равен {QUIET_ROOM}")

    elif CHIPPING_HAMMER >= noiseLevel >= GAS_MOWER:
        print(f"Уровень шума между {CHIPPING_HAMMER} дБ и {GAS_MOWER} дБ")
    elif GAS_MOWER >= noiseLevel >= ALARM_CLOCK:
        print(f"Уровень шума между {GAS_MOWER} дБ и {ALARM_CLOCK} дБ")
    elif ALARM_CLOCK >= noiseLevel >= QUIET_ROOM:
        print(f"Уровень шума между {ALARM_CLOCK} дБ и {QUIET_ROOM} дБ")
