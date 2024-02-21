from math import sqrt

a = int(input("Valeur de A : "))
b = int(input("Valeur de B : "))
c = int(input("Valeur de C : "))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (b * (-1) + sqrt(delta)) / (2 * a)
    x2 = (b * (-1) - sqrt(delta)) / (2 * a)
    print("2 solution dans R :")
    print(x1)
    print(x2)
elif delta == 0:
    x = (b * (-1)) / (2 * a)
    print("1 solution dans R :")
    print(x)
else:
    print("Pas de solutions dans R")
