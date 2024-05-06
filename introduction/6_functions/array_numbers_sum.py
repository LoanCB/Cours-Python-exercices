def somme_tableau(list: list[int]) -> int:
  sum = 0
  for number in list:
    sum += number
  return sum

numbers = [1, 7, 2, 5, 2]
print(somme_tableau(numbers))
