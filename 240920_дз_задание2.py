#Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Введите время в секундах: '))
# Перевод секунд в часы, минуты, секунды
hours = seconds // 3600
minutes = seconds // 60 - hours*60
seconds = seconds % 60
# Для красоты вывода добавление 0 в случае , если единицы времени менее 10
if hours < 10:
    HH = '0' + str(hours)
else:
    HH = str(hours)
if minutes < 10:
    MM = '0' + str(minutes)
else:
    MM = str(minutes)
if seconds < 10:
    SS = '0' + str(seconds)
else:
    SS = str(seconds)
# Вывод времени на экран
print (f'Точное время {HH}:{MM}:{SS}')