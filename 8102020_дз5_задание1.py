# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
out_f = open("out_file_task1.txt", "w")
my_string = '1'
while my_string != '':
    my_string = input('Введите строку: ')
    out_f.writelines(my_string + '\n')
out_f.close()
