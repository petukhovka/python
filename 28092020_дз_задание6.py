# ввод данных по продукту для универсальности в цикле по запрошенному у пользователя количеству товара,
#  можно и хардкодом, но количество товара жестко не указано в условии

#функция создания словаря по каждому продукту
def data(item):
    data = {'название':item[0], 'цена':item[1], 'количество':item[2], 'ед.изм':item[3]}
    return (data)

#функция наполнения содержимого списков сущностей по ключам готовой структуры
def content(key, length):
    list = []
    for i in range(length):
        list.append(result[i][1][key])
    return list

qty = int(input('Введите количество позиций товаров: '))
items = []
for i in range(qty):
    char = input('Введите через пробел Название, Цена, Количество, Единица измерения товара : ')
    elem = char.split(' ')
    items.append(elem)
# список продуктов
products = []
for i in range(qty):
    products.append(data(items[i]))
# результирующий список кортежей продуктов
result = []
for i,product in enumerate(products,1):
    duple = (i, product)
    result.append(duple)
print(result)

# вторая часть задачи про аналитику
itog = {}
for key in result[0][1]:
    itog[key] = content(key, len(result))

print(itog)
