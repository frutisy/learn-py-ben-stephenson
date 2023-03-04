from math import log10

a = int(input("a = "))
b = int(input("b = "))

amount = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b
log10a = log10(a)
exponential = a**b

print(f"a + b = {a} + {b} = {amount}")
print(f"a - b = {a} - {b} = {difference}")
print(f"a * b = {a} * {b} = {product}")
print(f"a / b = {a} / {b} = {quotient}")
print(f"a % b = {a} % {b} = {remainder}")
print(f"log10(a) = log10({a}) = {log10a}")
print(f"a**b = {a}**{b} = {exponential}")
