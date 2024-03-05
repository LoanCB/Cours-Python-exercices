USER_NUMBER = int(input("Veillez choisir un nombre entre 10 et 20 : "))
total = 0
count = 0

if not (10 <= USER_NUMBER <= 20):
    print("Le nombre choisi doit être compris entre 10 et 20 !")
else:
    while count != USER_NUMBER:
        count += 1
        total += count

    print(total)
