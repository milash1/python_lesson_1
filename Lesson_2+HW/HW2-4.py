idea = input('напишите, о чем думаете - ')
print(type(idea))
data = idea.split()
print(data)
for i, item in enumerate(data, 1):#взято из урока 3 в ответах
  print(f'{i} - {item}')