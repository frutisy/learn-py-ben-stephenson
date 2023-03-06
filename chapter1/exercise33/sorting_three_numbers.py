number1 = int(input("Введите первое целое число: "))
number2 = int(input("Введите второе целое число: "))
number3 = int(input("Введите третье целое число: "))

maxNumber = max(number1, number2, number3)
minNumber = min(number1, number2, number3)

print(f"Введённые вами числа, расположенные в порядке возрастания: "
      f"{minNumber}, "
      f"{number1 + number2 + number3 - minNumber - maxNumber}, "
      f"{maxNumber}")
