VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
user_letter = input("Saisir une lettre : ")
print(f"{user_letter} est une {'voyelle' if user_letter.lower() in VOWELS else 'consonne'}")