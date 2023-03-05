from math import radians
from math import acos
from math import sin
from math import cos

OVERAGE_VALUE_EARTH_RADIUS_IN_KMS = 6371.01

t1 = radians(int(input("Введите t1 (в градусах): ")))
g1 = radians(int(input("Введите g1 (в градусах): ")))
t2 = radians(int(input("Введите t2 (в градусах): ")))
g2 = radians(int(input("Введите g2 (в градусах): ")))

distance = round(OVERAGE_VALUE_EARTH_RADIUS_IN_KMS *
                 acos(sin(t1) * sin(g1) + cos(t1) * cos(t2) * cos(g1 - g2)), 2)

print(f"Расстояние между точками ({round(t1, 2), round(g1, 2)}) и "
      f"({round(t2, 2), round(g2, 2)}) при следовании по кратчайшему пути "
      f"по поверхности планеты \nравен {distance} км")
