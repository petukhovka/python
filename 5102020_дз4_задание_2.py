# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор списка.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = []
# С помощью цикла
for i in range(len(source_list)):
    if i < len(source_list)-1:
        if  source_list[i+1] > source_list[i]:
           result_list.append(source_list[i+1])
    else:
        break
print(result_list)

# С помощью генератора
result_list = [source_list[i+1] for i in range(len(source_list))
               if i<len(source_list)-1 and source_list[i+1] > source_list[i] ]
print(result_list)
