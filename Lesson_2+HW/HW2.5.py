my_list = [8, 7, 5, 5, 3, 2, 1]
new_number = int(input('Введите новый элемент рейтинга нат число - '))
i = 0

for n in my_list:
  if new_number <= n:
    i += 1

  elif new_number > n:
    break

my_list.insert(i, int(new_number))
print(my_list)