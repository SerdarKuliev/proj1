#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20


my_list = input("Введи данные: ")
print(my_list)
n = 0
my_list[n], my_list[n+1] = my_list[n+1], my_list[n]
my_list[n+2], my_list[n+3] = my_list[n+3], my_list[n+2]
my_list[n+4], my_list[n+5] = my_list[n+5], my_list[n+4]
my_list[n+6], my_list[n+7] = my_list[n+7], my_list[n+6]
my_list[n+8], my_list[n+9] = my_list[n+9], my_list[n+8]


print("Кажется получилось: "+ str(my_list))

