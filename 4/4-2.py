#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
##Результат: [12, 44, 4, 10, 78, 123].
new_list = (300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55)
list = []
for i in range(len(new_list)-1):
    if new_list[i] < new_list[i+1]:
        list.append(new_list[i+1])
print(list)
