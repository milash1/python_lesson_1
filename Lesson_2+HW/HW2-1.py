variety_list = ['String', 42, (5,25)]
variety_list = list(variety_list)
count = 0
while count < len(variety_list):
  print(type(variety_list[count]))
  count += 1
  