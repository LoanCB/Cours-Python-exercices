# Supprimer les n premiers caractères

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print(remove_chars("Loan est un super Prof !", 4))