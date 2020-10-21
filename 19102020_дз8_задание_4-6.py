# для сокращения кода опишем два типа офисной техники - принтер и ксерокс, но можно сколько угодно.
# вызов методов размещения и выдачи из методов классов в соотвествии с типом обрудования,
# само размещение/выдача/валидация происходитв классе склад
# данные по товару записыаем в словарь
from random import randint

class Stock:
    # метод размещения товара на складе
    @classmethod
    def stock_in(cls, equip, quantity):
        if Stock.valid(quantity): # - проверка на валидность в отдельном статикметоде, для простоты только на строковый
                                  # ввод количетства товара, но можно отправлять и другие данные и проверять их
            place = randint(1,1000) # - генерим рандомный номер места на складе
            return f'Товар {equip} в количестве {quantity} единиц принят на склад, место номер {place}'
        else:
            print('Введите количетсво товара в числовом виде !!!')
            quit()
    # метод выдачи товара со склада
    @classmethod
    def stock_out(cls, equip, quantity, division):
        if Stock.valid(quantity): # - проверка на валидность в отдельном статикметоде, для простоты только на строковый
                                  # ввод количетства товара, но можно отправлять и другие данные и проверять их
            return f'Товар {equip} в количестве {quantity} единиц передан в подразделение {division}'
        else:
            print('Введите количетсво товара в числовом виде !!!')
            quit()
    # метод для валидации данных
    @staticmethod
    def valid(quantity): # - метод проверки на валидность данных
        if isinstance(quantity, int):
            return True

class OfficeEquipment:
    def __init__(self, color, model, status, brand):
        self.color = color
        self.model = model
        self.status = status
        self.brand = brand

class Xerox(OfficeEquipment):
    equip = {}
    def __init__(self, param_xr, qty, color, model, status, brand, division = ''):
        self.param_xr = param_xr
        self.qty = qty
        self.division = division
        super().__init__(color, model, status, brand)

    def xerox_in(self):
        self.equip['param'] = self.param_xr
        self.equip['color'] = self.color
        self.equip['model'] = self.model
        self.equip['status'] = self.status
        self.equip['brand'] = self.brand
        return Stock.stock_in(self.equip, self.qty)

    def xerox_out(self):
        self.equip['param'] = self.param_xr
        self.equip['color'] = self.color
        self.equip['model'] = self.model
        self.equip['status'] = self.status
        self.equip['brand'] = self.brand
        return Stock.stock_out(self.equip, self.qty, self.division)

class Printer(OfficeEquipment):
    equip = {}
    def __init__(self, param_pr, qty, color, model, status, brand, division = ''):
        self.param_pr = param_pr
        self.qty = qty
        self.division = division
        super().__init__(color, model, status, brand)

    def printer_in(self):
        self.equip['param'] = self.param_pr
        self.equip['color'] = self.color
        self.equip['model'] = self.model
        self.equip['status'] = self.status
        self.equip['brand'] = self.brand
        return Stock.stock_in(self.equip, self.qty)

    def printer_out(self):
        self.equip['param'] = self.param_pr
        self.equip['color'] = self.color
        self.equip['model'] = self.model
        self.equip['status'] = self.status
        self.equip['brand'] = self.brand
        return Stock.stock_out(self.equip, self.qty, self.division)

# ввод данных по товару для размещения на складе
# первый параметр в экземпляре класса - типа спеицфичный параметр для типов оргтехники
xr_in = Xerox('xerox123', 6, 'white', 'tx-1419', 'used', 'brother')
print(xr_in.xerox_in())
# ввод данных по товару для размещения товара с количеством товара в виде строки
#xr_in = Xerox('xerox123', '6', 'white', 'tx-1419', 'used', 'brother')
#print(xr_in.xerox_in())

pr_in = Printer('printer123', 3, 'white', 'rtx-333', 'new', 'HP')
print(pr_in.printer_in())
# ввод данных по товару для размещения товара с количеством товара в виде строки
#pr_in = Printer('printer123', '3', 'white', 'rtx-333', 'new', 'HP')
#print(pr_in.printer_in())

xr_out = Xerox('xerox456', 45, 'white', 'rx-300', 'new', 'kyocera', 'HR')
print(xr_out.xerox_out())

pr_out = Printer('printer456', 15, 'black', 'DX-300', 'used', 'kyocera', 'IT')
print(pr_out.printer_out())
