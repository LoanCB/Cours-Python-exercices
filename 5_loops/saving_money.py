PERCENTAGE = 1 + float(input("Veillez indiquer un nombre pour le pourcentage d'intérêt : ")) / 100
YEARS = int(input("Veillez indiquer le nombre d'années à épargner : "))
number = float(input("Veillez indiquer la somme concernée : "))

for year in range(1, YEARS + 1):
    number *= PERCENTAGE

print(round(number, 2), '€')
