VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
user_letter = input("Saisir une lettre : ").lower()

if (user_letter in VOWELS):
    print(f"{user_letter} est une voyelle")
elif user_letter >= 'a' and user_letter <= 'z':
    print(f"{user_letter} est une consonne")
else:
    print(f"{user_letter} est un caractère spécial")
