person1 = {
    'prenom': 'Loan',
    'age': 21,
    'taille': 1.77,
    'homme': True,
}

print(person1)
print(person1.keys())
print(person1.values())
print(person1['age'])

person2 = {
    'prenom': 'Marie',
    'age': 47,
    'taille': 1.62,
    'homme': False,
}

persons = [person1, person2]
print(persons)
print(persons[1]['prenom'])
