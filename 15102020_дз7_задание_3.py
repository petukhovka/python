
class Cell:
    def __init__(self,qty):
        self.cell_qty = qty
    def __add__(self, other):
        return self.cell_qty + other.qty
    def __mul__(self, other):
        return self.cell_qty * other.qty
    def __truediv__(self, other):
        # по условию не вполне ясно,поэтому будем делить большее на меньшее, а не первое на второе и никак иначе
        if self.cell_qty >= other.cell_qty:
            return round(self.cell_qty / other.cell_qty )
        else:
            return round(other.cell_qty / self.cell_qty)
    def __sub__(self, other):
        # по условию не вполне ясно,поэтому будем вычитать из большего меньшее, а не первое на второе и никак иначе
        if self.cell_qty >= other.cell_qty:
            return round(self.cell_qty - other.cell_qty )
        else:
            return round(other.cell_qty - self.cell_qty)

    @property
    def qty(self):
        return self.cell_qty

    def make_order(self):
        str = ''
        for i in range(self.cell_qty // 5):
            str = str + '*****\n'
        return (str + '*' * (self.cell_qty % 5))

# один способ через методы перегрузки, второй (короче для мат операций) через декоратор
c1 = Cell(32)
c2 = Cell(44)
#Сумма ячеек
print(f'Сумма ячеек клеток: {c1 + c2}')
# сумма второй способ сумма через @property
print(f'Сумма ячеек клеток: {c1.qty + c2.qty}')

#Умножение
print(f'Произведение ячеек клеток: {c1 * c2}')
# второй способ
print(f'Произведение ячеек клеток: {c1.qty * c2.qty}')

#Деление
print(f'Частное ячеек клеток: {c1/ c2}')
#второй способ логика деления в теле программы
if c1.qty >= c2.qty:
    print(f'Частное ячеек клеток: {round(c1.qty / c2.qty)}')
else:
    print(f'Частное ячеек клеток: {round(c2.qty / c1.qty)}')

#Вычитание
print(f'Разность ячеек клеток: {c1 - c2}')
#второй способ логика деления в теле программы
if c1.qty >= c2.qty:
    print(f'Разность ячеек клеток: {round(c1.qty - c2.qty)}')
else:
    print(f'Разность ячеек клеток: {round(c2.qty - c1.qty)}')

# строка с ячейками по 5 штук
c3 = Cell(12)
print(c3.make_order())





