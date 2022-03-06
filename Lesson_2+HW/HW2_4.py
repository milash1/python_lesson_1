sentence = input('Введите слова через пробелы - ').split()
for i, word in enumerate(sentence, 1):
  print(f'{i}. {word[:10]}')