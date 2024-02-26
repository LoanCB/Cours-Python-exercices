VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
user_letter = input("Saisir une lettre : ")

if (user_letter.lower() in VOWELS):
    print(f"{user_letter} est une voyelle")
else:
    print(f"{user_letter} est une consonne")
