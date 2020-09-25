#Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.

a = float(input('Введите результат первого дня, км: '))
b = float(input('Введите целевой результат, км: '))
d = 1
print('Результат: ')
while a < b:
    print(f'{d}-й день: {round(a,2)}')
    a = a + a/10
    d += 1
print(f'{d}-й день: {round(a,2)}')
print(f'Ответ: на {d}-й день спортсмен достиг результата — не менее {b} км.')

