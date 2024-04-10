from random import randint

total_nine = 0
total_ten = 0
n = 100

for i in range(n):
    first = randint(1, 6)
    second = randint(1, 6)
    third = randint(1, 6)
    sum = first + second + third
    if sum == 9:
        total_nine += 1
    elif sum == 10:
        total_ten += 1

nine_percentage = round(total_nine / n * 100, 3)
ten_percentage = round(total_ten / n * 100, 3)

print(f"Nombre total d'occurences : {n}")
print(f"Nombre de sortie de 9 : {nine_percentage}%")
print(f"Nombre de sortie de 10 : {ten_percentage}%")
