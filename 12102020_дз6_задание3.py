#Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#name, surname, position (должность), income (доход).
#Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
#например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
#В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
#дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
#(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
class Position(Worker):

    def get_full_name(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}'
    def get_total_income(self):
        total = self._income['wage'] + self._income['bonus']
        return f'Общий доход : {total}'

p = Position('Ivan', 'Ivanov', 'CIO', 100000, 50000)
print(p.get_full_name())
print(p.get_total_income())
print(p.position)
