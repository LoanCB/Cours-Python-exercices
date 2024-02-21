import math

ab = float(input("Valeur de AB : "))
ac = float(input("Valeur de AC : "))

bc_carre = ab ** 2 + ac ** 2  # OU bc_carre = pow(ab, 2) + pow(ac, 2)
bc = math.sqrt(bc_carre)
print(bc)
