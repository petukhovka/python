# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Data:
#    def __init__(self, date):
#        self.date_str = date
    @classmethod
    def split_date(cls, date_str):
        date = date_str.split('-')
        cls.day = int(date[0])
        cls.month = int(date[1])
        cls.year = int(date[2])
        return Data.validate(cls.day,cls.month,cls.year)

# валидацию делаем без февральских дат и 30-31 числа по месяцам для упрощения проверок, смысл понятен, год пусть будет только 2020
# хотя можно и диапазон воткнуть
    @staticmethod
    def validate(day,month,year):
        if (1 <= day <=31) and (1 <= month <= 12) and year == 2020:
            return f'Сегодня {day} число {month} месяца и {year} года'
        else:
            return f'НЕВАЛИДНАЯ ДАТА !!!'

print(Data.split_date('16-02-2020'))
print(Data.split_date('32-02-2020'))
print(Data.split_date('16-13-2020'))
print(Data.split_date('16-02-2021'))