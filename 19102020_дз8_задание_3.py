# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
class MyListNotDigit(Exception):
    @staticmethod
    def zeromethod():
        pass

mylist = []
while True:
    try:
        el = input('Введите элемент списка: ')
        if el == 'stop':
            break
        if not el.isdigit():
            raise MyListNotDigit("Вы ввели не число")
    except MyListNotDigit as err:
        print(err)
    else:
        mylist.append(el)

print(mylist)