# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки c помощью принадлежности {self.title}'
class Pen(Stationery):
    def draw(self):
        return f'Ручка {self.title} - это сила !!!'
class Pencil(Stationery):
    def draw(self):
        return f'Карандаш {self.title} - это двойная сила !!!'
class Handle(Stationery):
    def draw(self):
        return f'Маркер {self.title} - это тройная сила !!!'

p = Pen('Parker')
print(p.draw())

pl = Pencil('Koh-i-Noor')
print(pl.draw())

h = Handle('Komus')
print(h.draw())

s = Stationery('Brush')
print(s.draw())