# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Исходные списки можете инициализировать прямо в коде,
# но обязательно проверьте работоспособность, для пустого списка, списка из 1 элемента,
# списка с четным количеством элементов и с нечетным. (Опционально) Если получится, реализуйте обмен, как функцию.
def listcheck(list):
    for i in range(len(list)):
         if i%2 != 0:
            tmp = list[i]
            list[i] = list[i -1]
            list[i-1] = tmp
    return(list)

#list = [4, 8, 54, 32, 67, 89, 23, 112, 98]
#list = []
#list = [2]
#list = ['kolya', 'petya']
list = ['kolya', 'petya', 'vanya']
print(listcheck(list))


