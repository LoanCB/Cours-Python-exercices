PERCENTAGE = 1 + float(input("Veillez indiquer un nombre pour le pourcentage d'intérêt : ")) / 100
YEARS = int(input("Veillez indiquer le nombre d'années à épargner : "))
number = float(input("Veillez indiquer la somme concernée : "))

for year in range(0, YEARS):
    number *= PERCENTAGE

print(f"Argent total : {round(number, 2)}")
