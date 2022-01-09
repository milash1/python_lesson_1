my_list = [8, 7, 5, 3, 2, 5, 6]
data = sorted(my_list)
print(data)
data.reverse()
print(data)
num_1 = input('Введите нат число: ')
print(type(num_1))
print(type(data))
data.append(num_1)
print(data)
num_2 = input('Введите нат число: ')
data.append(num_2)
print(data)
#как введенные числа сделать не тип str а int?