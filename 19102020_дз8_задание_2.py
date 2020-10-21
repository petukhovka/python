# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class MyZeroDivision(Exception):
    @staticmethod
    def zeromethod():
        pass

d1 = input("Введите делимое: ")
d2 = input("Введите делитель: ")

try:
    dividend = float(d1)
    divider = float(d2)
    if divider == 0:
        raise MyZeroDivision("Вы ввели НОЛЬ!")
except ValueError:
    print("Вы ввели не число")
except MyZeroDivision as err:
    print(err)
else:
    print(f"Частное: {dividend/divider}")

