#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [0, 5, 7, 5, 3, 3, 2, 8, 15, 42, 58]
print(my_list)
my_list.sort(reverse = True)
print(my_list)
my_list.append(int(input("number: ")))
print(my_list)
my_list.sort(reverse = True)
print(my_list)
my_list.append(int(input("number: ")))
print(my_list)
my_list.sort(reverse = True)
print(my_list)
my_list.insert(10, 158)
print(my_list)
my_list.sort(reverse = True)
print(my_list)

ok = input("Не уверен что правильно сделал.")

