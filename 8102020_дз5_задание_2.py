# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# для простоты не будем проверять на пустые строки
with open("in_file_task2.txt") as f_obj:
    i = 0
    list = []
    for line in f_obj:
        i += 1
        list = line.split(' ')
        print(f'В строке {i} всего слов: {len(list)}')
    print(f'Количество строк в файле: {i}')