# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

out_f = open("out_file_task5.txt", "w")
for i in range(randint(1,10)):
    el = str(randint(1,5))
    out_f.writelines(el + ' ')
out_f.close()
list = []
with open("out_file_task5.txt") as f_obj:
    for line in f_obj:
        list = line.split(' ')
 # обрезаем последний пробел в списке, получившийся при записи элемент + пробел
    del(list[-1])
    result = [int(item) for item in list]
    print(sum(result))
