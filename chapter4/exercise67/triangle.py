def is_triangle(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False

    if (a >= b + c) or (b >= a + c) or (c >= a + b):
        return False

    return True


x = 6
y = 2
z = 1

if is_triangle(x, y, z):
    print("Треугольник существует")
else:
    print("Треугольник не существует")
