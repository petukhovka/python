# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open("in_file_task3.txt") as f_obj:
    s = 0
    i = 0
    list = []
    for line in f_obj:
        list = line.split(' ')
        s = s + float(list [1])
        i += 1
        if  float(list[1]) < 20:
            print(list[0])
    print(f'Средняя ЗП = {round(s/i,2)}')

