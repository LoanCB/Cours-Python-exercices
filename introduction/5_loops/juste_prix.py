from random import randrange

correct_number = randrange(1, 100)
number_of_tries = 0
game = True

while game:
    user_anwser = int(input("Donner un nombre :"))
    number_of_tries += 1
    if user_anwser == correct_number:
        game = False
    elif user_anwser > correct_number:
        print("Moins")
    else:
        print("Plus")

print("Bravo, tu as trouvé le nombre en", number_of_tries, "essaies")
