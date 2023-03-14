number = 1

for i in range(100):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz-Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(f"Текущее число: {number}")

    number += 1
