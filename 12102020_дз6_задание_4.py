# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.ispolise = is_polise
    def go(self):
        pass
    def stop(self):
        pass
    def turn(self, direction):
        self.direction = direction
        print(f'Движение по направлению: {self.direction}')
    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
    def polise(self):
        if  self.ispolise:
            return 'Внимание, полиция !!!!'
        else:
            return 'Не полиция'

class TownCar(Car):
    def show_speed(self):
        if  self.speed > 60:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ !')
        else:
            print(f'Скорость {self.speed} км/ч')
class WorkCar(Car):
    def show_speed(self):
        if  self.speed > 40:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ !')
        else:
            print(f'Скорость {self.speed} км/ч')
class SportCar(Car):
    pass
class PoliceCar(Car):
    pass

t = TownCar(70, 'blue', 'Skoda', False)
t.show_speed()
print(t.name)
print(t.color)
print(t.polise())
# будем отделять вызовы разных штук одного класса от других
print('_'*100)

w = WorkCar(30, 'blue', 'VW', False)
w.show_speed()
print(w.name)
print(w.color)
print(w.polise())
print('_'*100)

s = SportCar(270, 'blue', 'RangeRover', False)
s.show_speed()
print(s.ispolise)
print(s.polise())
print('_'*100)

p = PoliceCar(170, 'blue', 'RangeRover', True)
p.show_speed()
print(p.polise())
p.turn('юго-запад')
print('_'*100)
