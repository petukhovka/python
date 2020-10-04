# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def list_check(my_list):
    for i in range(len(my_list)):
        if  my_list[i].isdigit():
           my_list[i] = int(my_list[i])
           continue
        else:
           my_list = my_list[:i]
           break
    return(my_list)

result = []
while True:

    my_list = []
    digits= input('Введите числа через пробел: ')
    my_list = digits.split(' ')
    l = len(my_list)
    my_list = list_check(my_list)
    result = result + my_list
    print(sum(result))
    if  l > len((my_list)):
        break
