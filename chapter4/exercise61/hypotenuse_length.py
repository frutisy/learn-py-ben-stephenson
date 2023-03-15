from math import sqrt


def compute_hypotenuse_length(a: float, b: float) -> float:
    return sqrt(a**2 + b**2)


cathetus1 = float(input("Введите длину первого катета: "))
cathetus2 = float(input("Введите длину второго катета: "))

hypotenuseLength = round(compute_hypotenuse_length(cathetus1, cathetus2), 1)

print(f"Длина гипотенузы прямоугольного треугольника с катетами {cathetus1} и "
      f"{cathetus2} равна {hypotenuseLength}")
